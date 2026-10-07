from xml.dom import ValidationErr

from pydantic import Basemodel


class User:
    name: str
    age: int
    is_active: bool = True


u = User(name="samyak", age=12)
print(u.name)
print(u.age)
print(u.is_active)


"""coerscion is there in pydantic Coercion means converting a value to the 
declared type. After validation, u.id really is an int,
 so the rest of your code can trust the types."""
"""for 42 as str it take as int but id as abc as str it will give exception for it same for bool as true,yes,1,will work 
bool for false and 0,off will work but abc as bool wont"""
m = User(name="samyak", age="42")
print(u.name)
print(u.age)

try:
    User(name="raam", age="abc")
except ValidationErr as e:
    print(e)


#######################################################################################################
"""required ,defaults,optionals"""
from pydantic import BaseModel


class Product(BaseModel):
    name: str  # required
    age: int  # required
    desc: str | None = None  # optional, default = None
    tags: list[str] = []  # optional, default = []
    in_stock: bool = True  # optional, default = True


p = Product(
    name="samyak", age=21, desc="uhnih", tags=["sam", "dede", "eded"], in_stock="no"
)

print(p.name)

#####################################################################################################################
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, EmailStr, Httpurl


class Event(BaseModel):
    id: UUID
    when: datetime
    cost: Decimal
    website: Httpurl
    organizer: EmailStr
    status: Literal["draft", "published"]
    attendees: list[str]
    metadata: dict[str, int]
    location: tuple[float, float]


e = Event(
    id="a1b2c3d4-0000-4000-8000-000000000000",
    when="2026-10-05T10:30:00",  # string → datetime
    cost="19.99",
    website="https://example.com",
    organizer="a@b.com",
    status="draft",
    attendees=["x", "y"],
    metadata={"floor": 3},
    location=(22.7, 75.8),
)
print(e.when.year)


###############################################################
"""field function ge,lee,lt ,max_length,min_length"""
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Item name")
    price: float = Field(gt=0, description="Must be positive")
    quantity: int = Field(default=1, ge=1, le=100)
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{4}$", examples=["ABC-1234"])
    tags: list[str] = Field(default_factory=list)


l = Item(
    name="samyak", price=123.33, quantity=12, sku="huhn", tags=["samyak", "raj", "ised"]
)


###############################################################################
"""Nested models """


class Address(BaseModel):
    city: str
    pincode: str


class Customer(BaseModel):
    name: str
    address = Address
    past_address: list[Address] = []


c = Customer(
    name="sam",
    address={"city": "indore", "pincode": "452001"},
)
print(c.address.city)
#########################################################
from pydantic import BaseModel, field_validator
from pydantic import ValidationError


class Signup(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def clean_username(cls, v: str) -> str:
        v = v.strip().lower()

        if not v.isalnum():
            raise ValueError("Username must contain only letters and numbers")

        return v

    @field_validator
    @classmethod
    def clean_pass(cls, v: str) -> str:
        if len(v) > 8:
            raise ValidationErr("vakhsk")
        return "sucess"


########################################################################3\\
"""MODEL VALIDATOR NOPW """
from pydantic import model_validator


class DateRange(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_order(self):
        if self.end < self.start:
            raise ValueError("end must be >= start")
        return self
