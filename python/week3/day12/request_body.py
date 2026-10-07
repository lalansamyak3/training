from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Items(BaseModel):
    name: str
    price: float
    description: str | None = None
    in_stock: bool = True


@app.post("/items")
def create(item: Items):
    return {"recived": item, "price_withtax": item.price * 1.18}


"""ADDING valiadrtion too now using Field """


class Items1(BaseModel):
    name: str = Field(min_length=2, max_length=50, examples=["pen"])
    price: float = Field(gt=0, description="price be posy")
    tags: list[str] = []
    quantity: int = Field(default=1, ge=0, le=1000)


@app.post("/items1")
def cretae3(itmes: Items1):
    return {"reicived": itmes, "name": Items1.name, "age": itmes.age}


################################################################################
"""nested model in request body"""


class Address(BaseModel):
    city: str
    pincode: str = Field(pattern=r"^\d{6}$")


class Customer(BaseModel):
    name: str
    address: Address
    otheraddress: list[Address] = []


@app.post("/customer")
def create(customer: Customer):
    return customer


######################################################################################
from typing import Literal


class User(BaseModel):
    username: str


class Item2(BaseModel):
    age: int = Field(ge=0, le=100, title="ageis here")
    gender: str = Literal["male", "female"]


@app.put("/combo/{item_id}")
def combo(item_id: int, item: Item2, user: User):
    return {"item": item, "user": user}


#####################################################################################################
from fastapi import Body

"""body is 
used toapply direct validation to 
request odty we dont need to cretyae 
pydantic model and use it to vbalidate 
the json body end by the client """


@app.post("/score")
def score(value: Annotated[int, Body(ge=0, le=100)]):
    return {"value": value}  # body: 42


@app.post("/score2")
def score2(item: Annotated[Items, Body(embed=True)]):
    return item  # body: {"item": {...}}


#################################################################################################################
"""custom validators """
from pydantic import BaseModel, field_validator, model_validator


class SignUp(BaseModel):
    username: str
    password: str
    confirmpass: str

    @field_validator("username")
    @classmethod
    def no(cls, v: str) -> str:
        if " " in v:
            raise ValueError("username must contain space nottt")
        return v.lower()

    @model_validator(mode="After")
    def passmatch(self):
        if self.password != self.confirmpass:
            raise ValueError("passwprd dont match")
        return self


#####################################################################3
