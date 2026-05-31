
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users = []

@app.post("/users/", response_model=User, status_code=201)
def create_user(user: User):
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
def get_all_users():
    return users

@app.get("/users/{id}", response_model=User)
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{id}", response_model=User)
def update_user(id: int, user: User):
    for i, u in enumerate(users):
        if u.id == id:
            user.id = id
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{id}", status_code=204)
def delete_user(id: int):
    for i, user in enumerate(users):
        if user.id == id:
            del users[i]
            return
    raise HTTPException(status_code=404, detail="User not found")
