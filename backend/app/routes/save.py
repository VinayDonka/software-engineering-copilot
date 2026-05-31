from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.file_writer import (
    save_code
)

router = APIRouter()


class SaveRequest(BaseModel):
    repo_path: str
    filename: str
    code: str


@router.post("/save-file")
def save(request: SaveRequest):

    path = save_code(
        request.repo_path,
        request.filename,
        request.code
    )

    return {
        "saved_to": path
    }