from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

app = FastAPI()


class userin(BaseModel):
    name: str
    age: int
    password: str


class userout(BaseModel):
    name: str
    age: int


@app.post("/users", response_model=userout)
def create_user(user: userin):
    return user  # ✅ FastAPI filter


###########################################################################
"""withput creating pydantic model for response body we can use inbuild methods
to remove certain fields """
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    name: str
    age: int
    gender: str
    password: str


@app.post("/users", response_model=UserIn, response_model_exclude={"password"})
def create_user(user: UserIn):
    return user


"""Option	Effect
response_model_exclude_unset=True
	omit fields that weren't explicitly set
response_model_exclude_none=True	
omit fields that are None
response_model_exclude_defaults=True	omit fields equal to their default
response_model_include={"name"} / 
response_model_exclude={"price"}	
pick or remove fields
"""


"""from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    age: int
    gender: str
    password: str


class UserRead(BaseModel):
    id: int
    name: str
    age: int
    gender: str


# fake in-memory database (stores everything, including password)
users_db = [
    {"id": 1, "name": "Ravi", "age": 25, "gender": "male", "password": "secret123"},
    {"id": 2, "name": "Priya", "age": 22, "gender": "female", "password": "pass456"},
    {"id": 3, "name": "Amit", "age": 30, "gender": "male", "password": "abc789"},
]


@app.get("/users", response_model=list[UserRead])
def list_users():
    return users_db
    
    
    [
  {"id": 1, "name": "Ravi", "age": 25, "},
  {"id": 2, "name": "Priya", "age": 22, );
  {"id": 3, "name": "Amit", "age": 30, }
]
"""
