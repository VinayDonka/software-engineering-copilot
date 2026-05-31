from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health/db")
async def health_check_db():
    # Placeholder for database health check
    return JSONResponse({"status": "ok"})

@app.get("/health/ollama")
async def health_check_ollama():
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": "Say hello",
                "stream": False
            }
        )
        response.raise_for_status()
        return JSONResponse({"status": "ok", "response": response.json()})
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health/openai")
async def health_check_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set")
    return JSONResponse({"status": "ok", "api_key": api_key})
