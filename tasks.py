import datetime as dt
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

import yaml
from ghapi.all import GhApi
from invoke import UnexpectedExit, task

org = "sscu-budapest"
report_repo = "sscu-budapest.github.io"

_root = Path("docs")


(release_root, topic_root, repo_root, label_root, report_target,) = all_io_dirs = [
    _root / dirname
    for dirname in [
        "_releases",
        "_topics",
        "_repos",
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
class Topic:
    name: str
    topic_id: str
    plural: str


@dataclass
class Repo:
    name: str
    link: str
    description: str
    topic: Topic


@dataclass
class Release:
    title: str
    tag: str
    link: str
    date: str
    release_id: int
    topic: Topic
    repo: Repo

    @property
    def fpath(self):
        return release_root / f"{self.date}-{self.release_id}.md".replace(":", "-")


@dataclass
class Issue:
    title: str
    url: str
    num: int

    @property
    def fm(self):
        return {
            "layout": "page",
            "permalink": f"/reports/{self.num}",
            "nav_exclude": True,
        }

    @property
    def fpath(self):
        return report_target / f"{self.num}.md"


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


topics = [
    Topic("Dataset", "dataset", "Datasets"),
    Topic("Research Project", "research-project", "Research Projects"),
    Topic("Research Software", "research-software", "Research Software"),
]


@task
def build(ctx, commit=False):

    for d in all_io_dirs:
        ctx.run(f"rm -rf {d}")
        d.mkdir()

    topic_repos = []
    api = GhApi()
    parse_reports(api)
    all_repos = api.repos.list_for_org(org)

    releases = []
    for gh_repo in all_repos:
        time.sleep(5)
        repo_topics = api.repos.get_all_topics(org, gh_repo.name)
        for topic in topics:
            if topic.topic_id not in repo_topics.names:
                continue
            repo = Repo(gh_repo.name, gh_repo.svn_url, gh_repo.description, topic)
            topic_repos.append(repo)
            for release in api.repos.list_releases(org, repo.name, per_page=10):
                releases.append(
                    Release(
                        release.name,
                        release.tag_name,
                        release.html_url,
                        release.published_at,
                        release.id,
                        topic,
                        repo,
                    )
                )

    for r in releases:
        r.fpath.write_text(to_fm(r))

    for t in topics:
        (topic_root / f"{t.topic_id}.md").write_text(to_fm(t))

    for rep in topic_repos:
        (repo_root / f"{rep.name}.md").write_text(to_fm(rep))

    if commit:
        for d in [release_root, topic_root, repo_root, report_target]:
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
        issue_cls = Issue(issue.title, issue.html_url, issue_num)
        for label in issue.labels:
            lname = label.name
            lab_cls = labels.get(
                lname,
                Label(lname.title(), label.description, lname.replace(" ", ""), []),
            )
            lab_cls.issues.append(issue_cls)
            labels[lname] = lab_cls

        report_page = "\n".join([dic_to_fm(issue_cls.fm), report_str])
        issue_cls.fpath.write_text(report_page)

    for l in labels.values():
        l.write_collection()
        l.write_page()
