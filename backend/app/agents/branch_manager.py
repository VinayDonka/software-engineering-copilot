from git import Repo


def create_branch(
    repo_path,
    branch_name
):

    repo = Repo(repo_path)

    if branch_name in repo.heads:
        return branch_name

    new_branch = repo.create_head(
        branch_name
    )

    new_branch.checkout()

    return branch_name