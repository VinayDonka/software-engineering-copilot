from git import Repo


def push_branch(
    repo_path: str,
    branch_name: str
):

    repo = Repo(repo_path)

    origin = repo.remote(
        name="origin"
    )

    origin.push(
        branch_name
    )

    return (
        f"Pushed {branch_name}"
    )