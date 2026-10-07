from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..repositories import user_repository
from ..schemas import UserCreate, UserUpdate

"""
def get_all_users(db: Session):
    return user_repository.get_users(db)"""


def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return user_repository.get_users(db, skip, limit)


def get_user_by_id(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


def create_user(db: Session, user_data: UserCreate):
    existing_user = user_repository.get_user_by_email(db, user_data.email)

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    return user_repository.create_user(db, user_data)


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = user_repository.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if user_data.email is not None:
        existing_user = user_repository.get_user_by_email(db, user_data.email)

        if existing_user is not None and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

    return user_repository.update_user(db, user, user_data)


def delete_user(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    user_repository.delete_user(db, user)

    return {"message": "User deleted successfully"}
