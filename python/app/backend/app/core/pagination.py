import math
from typing import Any, Generic, List, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class PageParams:
    """Use as: params: PageParams = Depends()"""

    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        size: int = Query(10, ge=1, le=100, description="Items per page"),
    ):
        self.page = page
        self.size = size

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size


class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int


def build_page(items: list, total: int, params: PageParams) -> dict[str, Any]:
    return {
        "items": items,
        "total": total,
        "page": params.page,
        "size": params.size,
        "pages": math.ceil(total / params.size) if total else 0,
    }


'''
Yes, Videos 1–4 are already building the same project, but they focus on its foundation rather than registration and login. 

AYTA
+1

Video

What he builds

1. Getting Started

Creates the FastAPI app, adds basic routes, returns JSON, and displays dummy data.

2. HTML Frontend

Adds HTML templates so users can view pages in a browser.

3. Path Parameters

Adds dynamic URLs, input validation, and error handling.

4. Pydantic Schemas

Defines request/response schemas and adds an endpoint to create records.

When does persistent storage begin?

Video 1: Basic app and in-memory dummy data.

Videos 2–4: Builds out the pages, API behavior, and data validation.

Video 5: Connects SQLite using SQLAlchemy and creates database models and relationships.

Video 10: Implements registration and login using JWT authentication.

So, if you want to follow the complete project, start at Video 1. If your only goal is to understand how he stores data in a database, start at Video 5.

import math
from typing import Any, Generic, List, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class PageParams:
    """Use as: params: PageParams = Depends()"""

    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        size: int = Query(10, ge=1, le=100, description="Items per page"),
    ):
        self.page = page
        self.size = size

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size


class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int


def build_page(items: list, total: int, params: PageParams) -> dict[str, Any]:
    return {
        "items": items,
        "total": total,
        "page": params.page,
        "size": params.size,
        "pages": math.ceil(total / params.size) if total else 0,
    }explain what it is doing
…
This code implements pagination in FastAPI. Pagination means returning data in small pages instead of sending all records in one API response.

Imagine your database has 100 users. Instead of returning all 100 users at once, your API can return 10 users per page.

Page 1 → users 1–10

Page 2 → users 11–20

Page 3 → users 21–30

Let's understand each part of your code.

1. Imports and T
import math
from typing import Any, Generic, List, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")

math: Used to calculate the total number of pages using math.ceil().

Any: Allows values of any type in a type annotation.

Generic and TypeVar: Allow you to create a reusable response model for different data types.

List: Represents a list of items.

Query: Defines and validates URL query parameters.

BaseModel: Used to define a Pydantic response model.

T: A placeholder for a type, such as User, Product, or Task.

For example, Page[User] means a page containing user records, while Page[Product] means a page containing product records.

2. PageParams — receives pagination parameters
class PageParams:
    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        size: int = Query(10, ge=1, le=100, description="Items per page"),
    ):
        self.page = page
        self.size = size

This class controls which page the client wants and how many items should appear on it.

Parameter

Meaning

page

The page number requested; default is 1.

size

Number of items per page; default is 10.

ge=1

Value must be greater than or equal to 1.

le=100

Page size cannot exceed 100.

For example, the client requests:

GET /users?page=2&size=10
FastAPI receives page=2 and size=10.

The client can change these values through the URL without changing the Python code.

What does Query() do?
page: int = Query(1, ge=1)

This tells FastAPI that page is a query parameter, defaults to 1, and must be at least 1.

If a client sends ?page=0, FastAPI rejects the request with a validation error.

Important: PageParams must be used with FastAPI's Depends() to get its parameters from the request.

from fastapi import Depends

@app.get("/users")
def get_users(params: PageParams = Depends()):
    ...

3. The offset property — decides where to start
@property
def offset(self) -> int:
    return (self.page - 1) * self.size

The offset tells the database how many records to skip before returning the requested page.

Suppose the database contains 100 users and the page size is 10.

Page

Calculation

Offset

Records

1

(1 - 1) × 10

0

1–10

2

(2 - 1) × 10

10

11–20

3

(3 - 1) × 10

20

21–30

4

(4 - 1) × 10

30

31–40

Why subtract 1? Because the first page starts at offset 0, not offset 10.

You can use this value in a SQLAlchemy query:

stmt = select(User).offset(params.offset).limit(params.size)
users = db.scalars(stmt).all()

offset(10) skips the first 10 records.

limit(10) returns at most 10 records.

For consistent pagination, add an explicit order_by() to the query so the database returns records in a predictable order.

4. Page — defines the response structure
class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int

This Pydantic model describes the shape of the paginated response.

Field

Meaning

items

The records on the current page.

total

Total matching records in the database, not just the current page.

page

Current page number.

size

Requested page size.

pages

Total number of pages needed for all matching records.

For example, if there are 45 users and the page size is 10, the response could look like this:

{
  "items": [
    {"id": 11, "name": "Aarav"},
    {"id": 12, "name": "Diya"}
  ],
  "total": 45,
  "page": 2,
  "size": 10,
  "pages": 5
}

The example only shows two items to keep it short; in a real response, page 2 would normally contain 10 items if all those records exist.

Page[T] is generic, so the same structure can be reused for users, products, orders, and other resources.

5. build_page() — builds the response data
def build_page(items: list, total: int, params: PageParams) -> dict[str, Any]:
    return {
        "items": items,
        "total": total,
        "page": params.page,
        "size": params.size,
        "pages": math.ceil(total / params.size) if total else 0,
    }

This function takes three inputs:

items: The records retrieved for the requested page.

total: The total number of matching records in the database.

params: The requested page and page size.

It combines them into a dictionary for the API response.

How is pages calculated?
math.ceil(total / params.size) if total else 0

math.ceil() rounds a number up to the next whole number.

Total records

Page size

Calculation

Pages

45

10

ceil(45 / 10)

5

40

10

ceil(40 / 10)

4

21

10

ceil(21 / 10)

3

0

10

No records

0

Why round up? Because 45 records require four full pages of 10 plus one additional page containing 5 records.

The if total else 0 part avoids dividing by zero when there are no records. In this code, params.size is already constrained to be at least 1.

6. How everything works together
1. Client sends a request

GET /users?page=2&size=10

2. PageParams

Validates page and size; calculates offset = 10.

3. Database query

Skips 10 records and retrieves up to 10 records.

4. Count matching records

For example, 45 users match the query.

5. build_page()

Combines the records, total, current page, page size, and total pages.

7. How you might use it in your FastAPI project
Here is a simplified example showing the pieces together. It assumes you already have a SQLAlchemy User model and a database session dependency.

from fastapi import Depends
from sqlalchemy import select, func
from sqlalchemy.orm import Session

@app.get("/users", response_model=Page[UserRead])
def get_users(
    params: PageParams = Depends(),
    db: Session = Depends(get_db),
):
    total = db.scalar(
        select(func.count()).select_from(User)
    ) or 0

    items = db.scalars(
        select(User)
        .order_by(User.id)
        .offset(params.offset)
        .limit(params.size)
    ).all()

    return build_page(
        items=list(items),
        total=total,
        params=params,
    )

Here, UserRead is your Pydantic schema for displaying users, User is your SQLAlchemy model, and get_db supplies the database session.

One important distinction: Page is defined in your original code but isn't directly used inside build_page(). In the example above, FastAPI uses Page[UserRead] as the response model to validate and document the response.

In short: PageParams handles pagination inputs, offset calculates which records to skip, Page defines the response format, and build_page() assembles the pagination metadata with the records.'''
