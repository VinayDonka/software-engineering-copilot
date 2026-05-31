from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.code_generator import (
    generate_code
)

from app.agents.context_builder import (
    build_context
)

router = APIRouter()


class CodeRequest(BaseModel):
    task: str
    repo_path: str


@router.post("/generate-code")
def generate(request: CodeRequest):

    context = build_context(
        request.repo_path
    )

    code = generate_code(
        request.task,
        context
    )

    return {
        "code": code
    }