from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blogs, users, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)

models.Base.metadata.create_all(engine)


@app.get('/')
def root():
    return "welcome to my api"



