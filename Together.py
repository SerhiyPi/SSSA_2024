from ast import Return
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Dict
from sqlalchemy import engine
from sqlalchemy.pool import impl
from db import models
from db.database import engine
from router import user_router
import sys
import os
from router import user_router

app = FastAPI()
app.include_router(user_router)
users_db= {}

class user(BaseModel):
    email: EmailStr
    Password: str
    username: str

@app.post("/register")
async def register_user(user: user):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    if any(u["email"] == user.email for u in users_db.values()):
        raise HTTPException(status_code=400, detail="Email already registered")

    users_db[user.username] = {"email": user.email, "password": user.Password}
    return {"message": "User registered successfully", "user": {"username": user.username, "email": user.email}}

models.Base.metadata.create_all(bind=engine)
