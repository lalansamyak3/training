from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import service
from app.auth.schemas import (
    ForgotPasswordRequest,
    MessageResponse,
    ResetPasswordRequest,
    Token,
)
from app.core.database import get_db
from app.users.schemas import UserCreate, UserOut
from app.utils.email import send_reset_email

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    return service.register_user(db, data)


@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Swagger's login form calls the field "username"; we send the email there.
    return service.login(db, form.username, form.password)


@router.post("/forgot-password", response_model=MessageResponse)
def forgot_password(
    data: ForgotPasswordRequest,
    background: BackgroundTasks,
    db: Session = Depends(get_db),
):
    result = service.request_password_reset(db, data.email)
    if result:
        email, link = result
        background.add_task(send_reset_email, email, link)
    # Same answer either way, so attackers can't discover which emails exist.
    return {"message": "If that email is registered, a reset link has been sent."}


@router.post("/reset-password", response_model=MessageResponse)
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    service.reset_password(db, data.token, data.new_password)
    return {"message": "Password reset successful. You can now log in."}
