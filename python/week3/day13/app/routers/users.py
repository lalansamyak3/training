from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas import UserCreate, UserResponse, UserUpdate
from ..services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

"""
@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)"""


@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_all_users(db, skip, limit)


@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user_data)


@router.patch("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user_data)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(db, user_id)
