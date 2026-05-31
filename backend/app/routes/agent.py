from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.orchestrator import run_agent

router = APIRouter()


class AgentRequest(BaseModel):
    repo_path: str
    task: str


@router.post("/run-agent")
def run(request: AgentRequest):

    return run_agent(
        request.repo_path,
        request.task
    )