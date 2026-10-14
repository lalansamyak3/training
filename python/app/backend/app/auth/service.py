from typing import Optional

import jwt
from sqlalchemy.orm import Session

from app.auth.schemas import Token
from app.auth.security import (
    create_token,
    decode_token,
    fingerprint,
    hash_password,
    verify_password,
)
from app.core.config import settings
from app.core.exceptions import AppError
from app.users import crud as users_crud
from app.users.models import User
from app.users.schemas import UserCreate


def register_user(db: Session, data: UserCreate) -> User:
    if users_crud.get_by_email(db, data.email):
        raise AppError("Email already registered", 409)
    if users_crud.get_by_phone(db, data.phone_no):
        raise AppError("Phone number already registered", 409)
    if users_crud.get_by_aadhaar(db, data.aadhaar_no):
        raise AppError("Aadhaar number already registered", 409)
    return users_crud.create_user(db, data, hash_password(data.password))


def login(db: Session, email: str, password: str) -> Token:
    user = users_crud.get_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise AppError("Incorrect email or password", 401)
    if not user.is_active:
        raise AppError("Account is disabled", 403)

    token = create_token(
        str(user.id),
        "access",
        settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        extra={"role": user.role.value},
    )
    return Token(
        access_token=token, expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )


def request_password_reset(db: Session, email: str) -> Optional[tuple[str, str]]:
    """Returns (email, reset_link) if the user exists, else None."""
    user = users_crud.get_by_email(db, email)
    if not user or not user.is_active:
        return None
    token = create_token(
        str(user.id),
        "reset",
        settings.RESET_TOKEN_EXPIRE_MINUTES,
        extra={"fp": fingerprint(user.hashed_password)},
    )
    return user.email, f"{settings.FRONTEND_URL}/reset-password?token={token}"


def reset_password(db: Session, token: str, new_password: str) -> None:
    invalid = AppError("Invalid or expired reset token", 400)
    try:
        payload = decode_token(token, "reset")
        user = users_crud.get_by_id(db, int(payload["sub"]))
    except (jwt.PyJWTError, KeyError, ValueError):
        raise invalid

    if not user or payload.get("fp") != fingerprint(user.hashed_password):
        raise invalid

    user.hashed_password = hash_password(new_password)
    db.commit()


"""
    1. Imports
- Optional: Allows a function to return a value or None.
- jwt: Used to catch JWT-related errors when validating reset tokens.
- Session: Represents the SQLAlchemy database session used to access and update records.
- Token: Defines the structure of the login response.
- Security functions: Create and decode tokens, generate password fingerprints, hash passwords, and verify passwords.
- settings: Contains configuration such as token expiration times and the frontend URL.
- AppError: Represents application-specific errors with HTTP status codes.
- users_crud: Provides database operations for finding and creating users.
- User and UserCreate: Represent the database user model and validated registration data.
2. register_user()
This function registers a new user.
First, it checks whether the email address already exists. If it does, the function raises a 409 Conflict error.
Next, it checks whether the phone number is already registered. If so, it raises another 409 error.
It then checks the Aadhaar number in the same way.
If all three checks pass, the function hashes the user's password and passes the registration data and password hash to the database creation function.
Purpose: Prevent duplicate user registrations and ensure the password is stored as a hash rather than plain text.
3. login()
This function authenticates a user and generates an access token.
First, it searches for the user using their email address.
If the user does not exist or the supplied password does not match the stored password hash, it raises a 401 Unauthorized error. Using the same error message for both cases avoids revealing whether an email address is registered.
Next, it checks whether the account is active. If the account is disabled, it raises a 403 Forbidden error.
If both checks pass, it creates an access token containing:
- The user's ID as the subject.
- The token type, set to access.
- The configured expiration duration.
- The user's role as additional information.
Finally, it returns a Token response containing the access token and its lifetime in seconds.
For example, if the access token lasts 15 minutes, expires_in is 900 seconds.
Purpose: Verify the user's credentials and issue a token for accessing protected endpoints.
4. request_password_reset()
This function starts the password-reset process.
First, it searches for the user by email. If the user does not exist or the account is inactive, it returns None.
If the user is active, the function creates a reset token containing:
- The user's ID.
- The token type, set to reset.
- The reset-token expiration time.
- A password fingerprint stored in the fp claim.
The fingerprint connects the token to the user's current password hash.
Next, the function constructs a reset URL using the configured frontend URL and attaches the token as a query parameter.
It returns the user's email address and the reset link as a tuple.
Important: This function does not send the email itself. Another part of the application must call the email-sending function with the returned address and link.
5. reset_password()
This function completes the password-reset process.
It receives the reset token and the user's new password.
First, it creates a standard error to use when the reset token is invalid or expired.
Then it attempts to decode the token, requiring the token type to be reset. If decoding succeeds, it extracts the user ID from the token's subject and searches for that user in the database.
If the token is invalid, expired, missing required information, or contains an invalid user ID, the function raises the reset-token error.
Next, it checks two things:
- Whether the user still exists.
- Whether the fingerprint inside the token matches the fingerprint of the user's current password hash.
If either check fails, the token is rejected.
If both checks pass, the function hashes the new password, replaces the existing password hash, and commits the change to the database."""
