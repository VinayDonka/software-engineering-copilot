from fastapi import FastAPI

from app.routes.planner import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():

    return {
        "message": "Software Engineering Copilot"
    }
    

from app.routes.repository import router as repo_router

app.include_router(repo_router)


from app.routes.code import router as code_router

app.include_router(code_router)

from app.routes.save import (
    router as save_router
)

app.include_router(save_router)

from app.routes.agent import (
    router as agent_router
)

app.include_router(agent_router)

from app.routes.git import (
    router as git_router
)

app.include_router(git_router)