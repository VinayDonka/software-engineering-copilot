
from fastapi import FastAPI, Depends, Request, HTTPException
from jose import JWTError, decode
import jwt
import os
import secrets

app = FastAPI()

# Replace with your secret key
SECRET_KEY = os.environ.get("JWT_SECRET", "your-secret-key")

def get_auth_header(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    return auth_header

def verify_jwt(auth_header):
    try:
        token = auth_header.split(" ")[1]
        decoded_payload = decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.get("/items/")
async def read_items(auth_header: str = Depends(get_auth_header)):
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    payload = verify_jwt(auth_header)
    
    if payload:
        return {"message": "Protected item accessed with JWT", "user_id": payload.get("user_id")}
    else:
        raise HTTPException(status_code=401, detail="Invalid JWT token")

@app.get("/public")
async def public_endpoint():
    return {"message": "This endpoint is public"}

@app.get("/protected")
async def protected_endpoint(auth_header: str = Depends(get_auth_header)):
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    payload = verify_jwt(auth_header)

    if payload:
        return {"message": "Protected endpoint accessed", "user_id": payload.get("user_id")}
    else:
        raise HTTPException(status_code=401, detail="Invalid JWT token")

@app.post("/login")
async def login(username: str, password: str):
    # In a real application, this would authenticate against a database
    # For simplicity, we'll use a hardcoded username and password
    if username == "testuser" and password == "password":
        payload = {
            "user_id": "testuser",
            "username": username
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return {"token": token}
    else:
        return {"error": "Invalid username or password"}
