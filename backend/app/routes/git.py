from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.git_manager import (
    commit_changes
)

router = APIRouter()


class CommitRequest(BaseModel):
    repo_path: str
    message: str


@router.post("/commit")
def commit(request: CommitRequest):

    sha = commit_changes(
        request.repo_path,
        request.message
    )

    return {
        "commit_sha": sha
    }