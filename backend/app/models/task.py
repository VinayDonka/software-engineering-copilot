from pydantic import BaseModel

class TaskRequest(BaseModel):
    task: str
    repo_path: str