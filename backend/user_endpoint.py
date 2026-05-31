from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health/db")
async def health_check_db():
    # Placeholder for database health check

@app.get("/hello")
async def hello():
    return {"message": "hello"}
