import uvicorn
from fastapi import FastAPI, FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/health/db")
async def health_check_db():
    # Placeholder for database health check
    return JSONResponse(status_code=200)

@app.get("/metrics")
async def metrics():
    return {
        "health_db": "ok"
    }

print('hello')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
