from fastapi import APIRouter

from app.models.task import TaskRequest
from app.agents.planner import generate_plan
from app.agents.context_builder import build_context

router = APIRouter()

@router.post("/plan")
def create_plan(request: TaskRequest):

    context = build_context(
        request.repo_path
    )

    result = generate_plan(
        request.task,
        context
    )

    return {
        "plan": result
    }