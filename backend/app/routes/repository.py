from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.repository_analyzer import (
    analyze_repository
)

router = APIRouter()


class RepositoryRequest(BaseModel):
    repo_path: str


@router.post("/analyze")
def analyze_repo(request: RepositoryRequest):

    result = analyze_repository(
        request.repo_path
    )

    return result