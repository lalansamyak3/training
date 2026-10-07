import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=18,
        description="Name must be between 3 and 18 characters",
    )

    email: EmailStr

    age: int = Field(
        gt=5, lt=100, description="Age must be greater than 5 and less than 100"
    )

    gender: Literal["male", "female"] = Field(
        description="Gender must be either male or female"
    )

    password: str = Field(
        min_length=8,
        max_length=8,
        description="Password must be exactly 8 characters with uppercase, lowercase, number and special symbol",
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")

        if not re.search(r"[^A-Za-z0-9]", value):
            raise ValueError("Password must contain at least one special character")

        return value


class UserUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=18,
        description="Name must be between 3 and 18 characters",
    )

    email: EmailStr | None = None

    age: int | None = Field(
        default=None,
        gt=5,
        lt=100,
        description="Age must be greater than 5 and less than 100",
    )

    gender: Literal["male", "female"] | None = Field(
        default=None, description="Gender must be either male or female"
    )

    password: str | None = Field(
        default=None,
        min_length=8,
        max_length=8,
        description="Password must be exactly 8 characters with uppercase, lowercase, number and special symbol",
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str | None) -> str | None:

        if value is None:
            return value

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")

        if not re.search(r"[^A-Za-z0-9]", value):
            raise ValueError("Password must contain at least one special character")

        return value


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    gender: Literal["male", "female"]

    model_config = ConfigDict(from_attributes=True)
