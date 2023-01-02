import datetime as dt
import os
from dataclasses import asdict, dataclass, field
from itertools import groupby
from pathlib import Path
from subprocess import check_call
from tempfile import TemporaryDirectory
from typing import List

import markdown
import requests
import yaml
from ghapi.all import GhApi
from invoke import UnexpectedExit, task

org = "sscu-budapest"
report_repo = f"{org}.github.io"

_root = Path("docs")


(
    contribs_root,
    projects_root,
    prospective_project_root,
    label_root,
    report_target,
) = all_io_dirs = [
    _root / dirname
    for dirname in [
        "_contributions",
        "_projects",
        "_prospective_projects",
        "_labels",
        "report_pages",
    ]
]

report_root = _root / "_reports"


def dic_to_fm(dic):
    return "\n".join(["---", yaml.dump(dic).strip(), "---"])


def to_fm(obj):
    return dic_to_fm(asdict(obj))


@dataclass
class Contributor:
    name: str
    last: str
    link: str


@dataclass
class Project:
    name: str
    repo_name: str
    last_version: str
    last_published: str
    readme: str

    @property
    def fpath(self):
        return projects_root / f"{self.name}.md"


@dataclass
class Contribution:
    link: str
    name: str
    latest: List[Contributor] = field(default_factory=list)

    @property
    def fpath(self):
        return contribs_root / f"{self.name}.md"


@dataclass
class Issue:
    title: str
    url: str
    num: int

    @property
    def fm(self):
        return {
            "layout": "page",
            "permalink": self.permalink,
            "nav_exclude": True,
        }

    @property
    def fpath(self):
        return report_target / f"{self.num}.md"

    @property
    def permalink(self):
        return f"/reports/{self.num}"


@dataclass
class ProspectiveProject:

    num: int
    title: str
    issue_url: str
    report_link: str

    @property
    def fpath(self):
        fname = f"{'a' if self.report_link else 'b'}{self.num}.md"
        return prospective_project_root / fname


@dataclass
class Label:
    title: str
    description: str
    id_: str
    issues: List[Issue]

    def fpath(self, parent):
        return parent / f"{self.id_}.md"

    def write_collection(self):
        self.fpath(label_root).write_text(to_fm(self))

    def write_page(self):
        self.fpath(report_target).write_text(
            dic_to_fm(
                {
                    "layout": "label",
                    "parent": "Reports",
                    **asdict(self),
                }
            )
        )


@task
def build(ctx, commit=False):

    for d in all_io_dirs:
        ctx.run(f"rm -rf {d}")
        d.mkdir()

    api = GhApi(token=os.environ.get("GH_TOKEN"))
    parse_reports(api)
    all_repos = api.repos.list_for_org(org)
    members = api.orgs.list_members(org)
    fork_sources = [api.repos.get(org, r.name).source for r in all_repos if r.fork]
    dump_contribs(fork_sources, members, api)
    dump_projects(api)

    if commit:
        for d in all_io_dirs:
            ctx.run(f"git add {d}")

        try:
            ctx.run(f'git commit -m "rebuild-{dt.date.today()}"')
            ctx.run("git push")
        except UnexpectedExit:
            pass


def parse_reports(api):
    labels = {}
    for report_fp in report_root.glob("*.md"):
        report_str = report_fp.read_text()
        issue_num = int(report_fp.name[:-3])
        issue = api.issues.get(org, report_repo, issue_num)
        issue_inst = Issue(issue.title, issue.html_url, issue_num)
        for label in issue.labels:
            lname = label.name
            lab_inst = labels.get(
                lname,
                Label(lname.title(), label.description, lname.replace(" ", ""), []),
            )
            lab_inst.issues.append(issue_inst)
            labels[lname] = lab_inst

        report_page = "\n".join([dic_to_fm(issue_inst.fm), report_str])
        issue_inst.fpath.write_text(report_page)

    for label in labels.values():
        label.write_collection()
        label.write_page()


def dump_contribs(fork_sources, members, api):
    for repo in fork_sources:
        owner = repo.owner.login
        rname = repo.name
        contrib = Contribution(repo.html_url, rname)
        for member in members:
            user_id = member.login
            commits = api.repos.list_commits(owner, rname, author=user_id)
            if not commits:
                continue
            _date = commits[0].commit.author.date[:10]
            _link = f"https://github.com/{owner}/{rname}/commits?author={user_id}"
            contrib.latest.append(Contributor(member.login, _date, _link))
        contrib.fpath.write_text(to_fm(contrib))


def dump_projects(api):
    tdir = TemporaryDirectory()
    check_call(["git", "clone", f"https://github.com/{org}/main-registry", tdir.name])
    for proj_name, vs in groupby(
        sorted(Path(tdir.name, "info").glob("*.yaml")), lambda p: p.name.split("-")[0]
    ):
        proj_dic = yaml.safe_load(Path(sorted(vs)[-1]).read_text())
        last_tag = sorted(
            proj_dic["tags"], key=lambda t: tuple(map(int, t.split("/")[2].split(".")))
        )[-1]
        _, v, tagid, __ = last_tag.split("/")  # zimmer-v0/0.0/2022.4.19.1/complete
        repo_name = proj_dic["uri"].split("/")[-1]
        readme_md = requests.get(
            f"https://raw.githubusercontent.com/{org}/{repo_name}/main/README.md"
        )
        readme = markdown.markdown(readme_md.text)
        p = Project(
            proj_name, repo_name, last_version=v, last_published=tagid, readme=readme
        )
        p.fpath.write_text(to_fm(p))
    tdir.cleanup()

    project_issues = api.issues.list_for_repo(
        org, report_repo, labels="new project", state="open"
    )

    for issue in project_issues:
        issue_inst = Issue(issue.title, issue.html_url, issue.number)
        report_link = issue_inst.permalink if issue_inst.fpath.exists() else ""
        pp = ProspectiveProject(
            issue_inst.num, issue_inst.title, issue_inst.url, report_link
        )
        pp.fpath.write_text(to_fm(pp))
