from fastapi import APIRouter
from starlette.routing import Router
from db import models
from db.database import get_db
from typing import List



router = APIRouter(prefix='/users', tags=["users"])
user_router = APIRouter()

@user_router.get("/users")
def get_users():
   return {"message": "List of users"}

