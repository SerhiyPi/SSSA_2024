from schemas import UserBase
from fastapi import APIRouter, Depends
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user


router = APIRouter(prefix="/users", tags=["users"])

#Create a user

@router.post("/")
def create_user(request: UserBase, db: Session, Depends=(get_db)):
    return db_user.create_user(db: request)

#read a user

#@router.get("/{user_id}",tags=["users"])
#async def read_user(user_id: int):
    #return {"user_id": user_id}


#update a user

#@router.put("/{user_id}",tags=["users"])
#async def update_user(user_id: int):
    #return {"user_id": user_id}


#delete a user

#@router.delete("/{user_id}",tags=["users"])
#async def delete_user(user_id: int):
    #return {"user_id": user_id}   