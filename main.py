from fastapi import FastAPI
from router import blog_get
from router import blog_post
from db import models
from db.database import engine


@app.get('/hello')
def index():
    return {"message":'Welcome to LINKUP! This is a social network project. Developers team SSSA.'}
