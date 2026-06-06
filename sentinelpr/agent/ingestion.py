import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

def fetch_pr_diff(pr_number: int) -> dict:
    repo_name = os.getenv("GITHUB_REPO")
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    chunks = []
    for f in pr.get_files():
        chunks.append({
            "filename": f.filename,
            "status": f.status,
            "additions": f.additions,
            "deletions": f.deletions,
            "patch": f.patch or ""
        })

    return {
        "pr_number": pr_number,
        "title": pr.title,
        "author": pr.user.login,
        "body": pr.body,
        "base_branch": pr.base.ref,
        "head_branch": pr.head.ref,
        "files": chunks
    }

def pretty_print_diff(pr_dict: dict):
    print(f"\n{'='*60}")
    print(f"PR #{pr_dict['pr_number']}: {pr_dict['title']}")
    print(f"Author: {pr_dict['author']} | Base: {pr_dict['base_branch']}")
    print(f"Files changed: {len(pr_dict['files'])}")
    for f in pr_dict['files']:
        print(f"\n--- {f['filename']} ({f['status']}) ---")
        print(f"  +{f['additions']} additions, -{f['deletions']} deletions")
        if f['patch']:
            print(f['patch'][:500])
    print('='*60)