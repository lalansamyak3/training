import hashlib
from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
import jwt

from app.core.config import settings


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def fingerprint(hashed_password: str) -> str:
    """Ties a reset token to the current password so it works only once."""
    return hashlib.sha256(hashed_password.encode()).hexdigest()[:16]


def create_token(
    subject: str,
    token_type: str,
    expires_minutes: int,
    extra: Optional[dict] = None,
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,
        "type": token_type,
        "iat": now,
        "exp": now + timedelta(minutes=expires_minutes),
        **(extra or {}),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str, expected_type: str) -> dict:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    if payload.get("type") != expected_type:
        raise jwt.InvalidTokenError("Wrong token type")
    return payload


"""1. Imports
- hashlib generates a SHA-256 hash used for the password fingerprint.
- datetime, timedelta, and timezone handle token creation and expiration times.
- Optional allows a value to be either a particular type or None.
- bcrypt hashes passwords and verifies them.
- jwt creates and decodes JWT tokens.
- settings provides configuration values such as the secret key and signing algorithm.
2. hash_password()
This function takes a user's plain-text password and converts it into a bcrypt hash.
For example, when a user registers, the application hashes their password before storing it in the database.
The original password is not stored directly. Bcrypt also uses a random salt, so the same password can produce different hashes on separate calls.
3. verify_password()
This function checks whether a password entered by the user matches the password hash stored in the database.
For example, during login, the application retrieves the stored hash and verifies the entered password against it.
It returns True if the password matches and False otherwise.
4. fingerprint()
This function creates a short fingerprint from the existing password hash using SHA-256.
Its purpose is to connect a password-reset token to the user's current password hash.
For example:
- When the reset token is created, the application includes a fingerprint of the current password hash.
- If the password changes, the password hash changes.
- The application calculates a new fingerprint and compares it with the fingerprint in the token.
- If they differ, the old token can be rejected.
This can help invalidate reset tokens after a password change, provided the reset workflow performs that comparison.
5. create_token()
This function creates a JWT for a particular user and purpose.
It accepts four inputs:
- Subject: Identifies the user, usually through their user ID.
- Token type: Identifies the token's purpose, such as access, refresh, or reset.
- Expiration duration: Specifies how many minutes the token remains valid.
- Extra data: Optional additional information to include in the token.
It records the current UTC time and builds the token payload.
The payload contains:
- sub: The identity of the user.
- type: The purpose of the token.
- iat: The time when the token was issued.
- exp: The time when the token expires.
- Additional claims, if provided.
It then signs the payload using the configured secret key and algorithm and returns the encoded JWT.
For example, the same function can create a short-lived access token or a password-reset token by changing the token type and expiration duration.
6. decode_token()
This function validates a JWT and returns its decoded payload.
It performs two main checks:
1. JWT validation: Checks the token's signature and expiration.
2. Token-purpose validation: Compares the token's type with the expected type.
For example, if an endpoint expects a reset token but receives an access token, the function rejects it.
If validation succeeds, the decoded payload is returned so the application can read the user's ID and other claims.
If validation fails, the JWT library raises an error."""
