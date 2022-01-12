import datetime as dt
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml
from ghapi.all import GhApi
from invoke import UnexpectedExit, task

org = "sscu-budapest"
report_repo = "sscu-budapest.github.io"


release_root = Path("docs", "_releases")
topic_root = Path("docs", "_topics")
repo_root = Path("docs", "_repos")
report_root = Path("docs", "_reports")
report_target = Path("docs", "reports")


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

    def get_fname(self):
        return f"{self.date}-{self.release_id}.md".replace(":", "-")


topics = [
    Topic("Dataset", "dataset", "Datasets"),
    Topic("Research Project", "research-project", "Research Projects"),
    Topic("Research Software", "research-software", "Research Software"),
]


@task
def build(ctx, commit=False):

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

    for d in [release_root, topic_root, repo_root]:
        ctx.run(f"rm -rf {d}")
        d.mkdir()

    for r in releases:
        fname = r.get_fname()
        (release_root / fname).write_text(to_fm(r))

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

    for report_fp in report_root.glob("*.md"):
        report_str = report_fp.read_text()
        issue_num = int(report_fp.name[:-3])

        issue = api.issues.get(org, report_repo, issue_num)

        new_fm = {
            "issue_url": issue.html_url,
            "issue_title": issue.title,
            "issue_labels": [l.name for l in issue.labels],
            "layout": "page",
            "permalink": f"/reports/{issue_num}",
            "parent": "Reports",
        }

        (report_target / f"{issue_num}.md").write_text(
            "\n".join(dic_to_fm(new_fm), report_str)
        )
