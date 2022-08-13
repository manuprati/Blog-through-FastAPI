from fastapi import Depends, APIRouter, HTTPException
from .. import schemas, models, database
from ..hashing import Hash
from typing import List
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    tags=['User'],
    prefix='/users'
)



@router.post('/')#, response_model=schemas.ShowUser)
def create_user(req: schemas.User, db: Session = Depends(database.get_db)):
    
    return user.create(req,db)

@router.get('/', response_model=List[schemas.ShowUser])
def get_user(db: Session = Depends(database.get_db)):
    return user.all(db)