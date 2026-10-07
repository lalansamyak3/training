from datetime import datetime

from python.week3.day1.pydantic1 import BaseModel, EmailStr, ConfigDict, Field


class PostBase(BaseModel):

    title: str = Field(min_length=1, max_length=100)

    content: str = Field(min_length=1)

    # author:str=Field(min_length=1,max_length=50)


class PostCreate(PostBase):

    user_id: int


class PostResponse(PostBase):

    model_config = ConfigDict(from_attributes=True)

    id: int

    user_id: int

    date_posted: datetime

    author: UserResponse


class UserBase(BaseModel):

    username: str = Field(min_length=1, max_length=50)

    email: EmailStr = Field(max_length=120)


class UserCreate(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int

    image_file: str | None

    image_path: str


"""pydamtioc can read from sqlaldchemy model thats why it is true """


class UserResponse(UserBase):

    pass
