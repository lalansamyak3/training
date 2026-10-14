from datetime import date, datetime
from typing import Annotated, Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_serializer,
    field_validator,
    model_validator,
)

from app.core.validators import calculate_age, validate_password_strength
from app.users.enums import Gender, Occupation, Role

# ---------- reusable constrained types ----------
NameStr = Annotated[
    str,
    Field(
        min_length=2,
        max_length=100,
        pattern=r"^[A-Za-z]+(?: [A-Za-z]+)*$",
        description="Letters and spaces only, no digits",
    ),
]
AgeInt = Annotated[
    int, Field(strict=True, ge=10, le=100, description="Whole number 10-100")
]
PhoneStr = Annotated[str, Field(pattern=r"^\d{10}$", description="Exactly 10 digits")]
AadhaarStr = Annotated[
    str, Field(pattern=r"^[2-9]\d{11}$", description="12-digit Aadhaar")
]
PlaceStr = Annotated[
    str, Field(min_length=2, max_length=60, pattern=r"^[A-Za-z]+(?:[ .'-][A-Za-z]+)*$")
]
StreetStr = Annotated[str, Field(min_length=3, max_length=200)]


def _dob_not_in_future(value: date) -> date:
    if value > date.today():
        raise ValueError("Date of birth cannot be in the future")
    return value


# ---------- create (registration) ----------
class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: NameStr
    age: AgeInt
    gender: Gender
    dob: date = Field(description="Format: YYYY-MM-DD", examples=["2000-01-31"])
    phone_no: PhoneStr
    email: EmailStr
    occupation: Occupation
    street: Optional[StreetStr] = None
    city: PlaceStr
    state: PlaceStr
    country: PlaceStr
    aadhaar_no: AadhaarStr
    password: str
    confirm_password: str

    _check_dob = field_validator("dob")(_dob_not_in_future)

    @field_validator("email")
    @classmethod
    def lower_email(cls, v: str) -> str:
        return v.lower()

    @field_validator("password")
    @classmethod
    def strong_password(cls, v: str) -> str:
        return validate_password_strength(v)

    @model_validator(mode="after")
    def cross_checks(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        if calculate_age(self.dob) != self.age:
            raise ValueError("Age does not match the date of birth")
        return self


# ---------- update (everything Optional) ----------
class UserUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: Optional[NameStr] = None
    age: Optional[AgeInt] = None
    gender: Optional[Gender] = None
    dob: Optional[date] = None
    phone_no: Optional[PhoneStr] = None
    occupation: Optional[Occupation] = None
    street: Optional[StreetStr] = None
    city: Optional[PlaceStr] = None
    state: Optional[PlaceStr] = None
    country: Optional[PlaceStr] = None

    @field_validator("dob")
    @classmethod
    def dob_check(cls, v: Optional[date]) -> Optional[date]:
        return _dob_not_in_future(v) if v else v


class AdminUserUpdate(UserUpdate):
    role: Optional[Role] = None
    is_active: Optional[bool] = None


# ---------- response ----------
class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    gender: Gender
    dob: date
    phone_no: str
    email: EmailStr
    occupation: Occupation
    street: Optional[str]
    city: str
    state: str
    country: str
    aadhaar_no: str
    photo_url: Union[str, None]
    role: Role
    is_active: bool
    created_at: datetime

    @field_serializer("aadhaar_no")
    def mask_aadhaar(self, value: str) -> str:
        return "XXXXXXXX" + value[-4:]


"""Let's break it down:
- @field_serializer("aadhaar_no") — applies this serializer to the aadhaar_no field.
- value: str — receives the original Aadhaar number.
- value[-4:] — extracts the last four characters.
- "XXXXXXXX" + value[-4:] — combines eight X characters with those last four digits."""
