from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..hashing import Hash
from typing import List

def create(req,db):
    user = models.User(name=req.name, email=req.email, password=Hash.bcrypt(req.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user created":user}


def all(db):
    user = db.query(models.User).all()
    return user