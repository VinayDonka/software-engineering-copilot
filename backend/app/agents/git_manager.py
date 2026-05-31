from git import Repo
from git.exc import InvalidGitRepositoryError


def commit_changes(
    repo_path: str,
    message: str
):

    try:

        repo = Repo(repo_path)

        repo.git.add(A=True)

        commit = repo.index.commit(
            message
        )

        return commit.hexsha

    except InvalidGitRepositoryError:

        return "ERROR: Not a Git repository"