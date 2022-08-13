from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog

def create(request, db: Session):
    blog = models.Blog(title=request.title, body = request.body)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def destroy(db: Session, id: int):
    queryBlog = db.query(models.Blog).filter(models.Blog.id == id)
    blog = queryBlog.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog with id {id} does not exist')

    queryBlog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_one(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog with id {id} does not exits')

    return blog

def modify(id: int, db:Session, request ):
    blog = db.query(models.Blog).filter(models.Blog.id == id,)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog with id {id} does not exits')

    blog.update(request)
    db.commit()
    return "updated" #blog.first()