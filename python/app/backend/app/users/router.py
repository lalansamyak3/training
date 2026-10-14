from typing import Optional, Union

from fastapi import APIRouter, Depends, File, Query, UploadFile
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_admin, get_current_user
from app.core.database import get_db
from app.core.exceptions import AppError
from app.core.pagination import Page, PageParams, build_page
from app.users import crud
from app.users.enums import Gender, Occupation
from app.users.models import User
from app.users.schemas import AdminUserUpdate, UserOut, UserUpdate
from app.utils.file_upload import delete_photo, save_photo

router = APIRouter(prefix="/users", tags=["Users"])


# ---------- logged-in user (own profile) ----------
@router.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/me", response_model=UserOut)
def update_me(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud.update_user(db, current_user, data)


@router.post("/me/photo", response_model=UserOut)
async def upload_my_photo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_url = await save_photo(file)
    delete_photo(current_user.photo_url)
    current_user.photo_url = new_url
    db.commit()
    db.refresh(current_user)
    return current_user


# ---------- admin only ----------
@router.get("", response_model=Page[UserOut])
def list_users(
    params: PageParams = Depends(),
    search: Optional[str] = Query(
        None, max_length=100, description="Name, email or phone"
    ),
    gender: Optional[Gender] = None,
    occupation: Optional[Occupation] = None,
    city: Union[str, None] = None,
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin),
):
    items, total = crud.list_users(db, params, search, gender, occupation, city)
    return build_page(items, total, params)


@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin),
):
    user = crud.get_by_id(db, user_id)
    if not user:
        raise AppError("User not found", 404)
    return user


@router.patch("/{user_id}", response_model=UserOut)
def admin_update_user(
    user_id: int,
    data: AdminUserUpdate,
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin),
):
    user = crud.get_by_id(db, user_id)
    if not user:
        raise AppError("User not found", 404)
    return crud.update_user(db, user, data)


@router.delete("/{user_id}", status_code=204)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin),
):
    user = crud.get_by_id(db, user_id)
    if not user:
        raise AppError("User not found", 404)
    if user.id == admin.id:
        raise AppError("Admins cannot delete their own account", 400)
    delete_photo(user.photo_url)
    crud.delete_user(db, user)
