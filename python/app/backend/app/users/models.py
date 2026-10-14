from datetime import date, datetime
from typing import Optional

from sqlalchemy import Boolean, Date, DateTime, String, func
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.users.enums import Gender, Occupation, Role


def _values(enum_cls):
    return [member.value for member in enum_cls]


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]
    gender: Mapped[Gender] = mapped_column(
        SAEnum(Gender, name="gender_enum", values_callable=_values)
    )
    # used for enum to accept value of enum name=gender_enum db coulumn will be gender_enum value_calllable +_value
    # _value take the enum class as parameter and help to fetch the value
    dob: Mapped[date] = mapped_column(Date)
    phone_no: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    occupation: Mapped[Occupation] = mapped_column(
        SAEnum(Occupation, name="occupation_enum", values_callable=_values)
    )
    street: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(60))
    country: Mapped[str] = mapped_column(String(60))
    aadhaar_no: Mapped[str] = mapped_column(String(12), unique=True)
    photo_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(
        SAEnum(Role, name="role_enum", values_callable=_values), default=Role.USER
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )


"""
def _values(enum_cls):
    return [member.value for member in enum_cls] enum_cls is If gender 
    then male.value =male ,female.value=femaele amd if enums_cls is occupation then 
    student.valeue=student etc"""
