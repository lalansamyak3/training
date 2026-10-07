from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserCreate, UserUpdate

"""
def get_users(db: Session):
    stmt = select(User)
    result = db.execute(stmt)

    return result.scalars().all()
    """


# for paginationation using inbuild method offstand and limit so cretaed again get_users()
def get_users(db: Session, skip: int = 0, limit: int = 10):
    stmt = select(User).offset(skip).limit(limit)

    result = db.execute(stmt)

    return result.scalars().all()


def get_user_by_id(db: Session, user_id: int):
    stmt = select(User).where(User.id == user_id)
    result = db.execute(stmt)

    return result.scalar_one_or_none()


def get_user_by_email(db: Session, email: str):
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt)

    return result.scalar_one_or_none()


def create_user(db: Session, user_data: UserCreate):
    user = User(
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        gender=user_data.gender,
        password=user_data.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user: User, user_data: UserUpdate):
    update_data = user_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()

    return user
