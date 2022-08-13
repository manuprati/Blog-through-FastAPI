from fastapi import Depends, status, APIRouter, HTTPException

from ..oauth2 import get_current_user
from .. import schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blogs',
    tags=['Blog']
)

# from ..router.database import SessionLocal, engine



@router.get('/',  response_model=List[schemas.BlogOut])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)
        
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogOut)
def get_one_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_one(db, id)
    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(db, id)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.modify(id, db, request)
