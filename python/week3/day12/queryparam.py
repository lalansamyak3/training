from fastapi import FastAPI

app = FastAPI()

from typing import Annotated

from fastapi import FastAPI, Query


@app.get("/items")
def read_items(skip: int = 0, limit: int = 10, q: str | None = None):
    return {"skip": skip, "limit": limit, "q": q}


@app.get("/search")
def search(
    q: str,  # REQUIRED (no default)
    category: str | None = None,  # optional
    in_stock: bool = True,
):  # optional with default
    result = {"q": q, "in_stock": in_stock}
    if category:
        result["category"] = category
    return result


from fastapi import Query


@app.get("/search")
def search(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=50,
            description="Search text",
            pattern="^[a-zA-Z ]+$",
        ),
    ] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
):
    return {"q": q, "limit": limit}


@app.get("/filter")
def filter_items(tags: Annotated[list[str] | None, Query()] = None):
    return {"tags": tags}


# GET /filter?tags=red&tags=blue  → {"tags": ["red", "blue"]}


@app.get("/legacy")
def legacy(
    item_query: Annotated[
        str | None, Query(alias="item-query")
    ] = None,  # URL uses "item-query"
    old_param: Annotated[
        str | None, Query(deprecated=True)
    ] = None,  # shown crossed-out in docs
    internal: Annotated[
        str | None, Query(include_in_schema=False)
    ] = None,  # hidden from docs
):
    return {"item_query": item_query}


from pydantic import BaseModel, Field


class detail(BaseModel):
    model_config = {"extra": "forbid"}
    name: str = Field(min_length=2, max_length=12)
    age: int = Field(10, ge=0, le=100)
    prder_by: str = "created_at"


@app.get("/things")
def list_things(filters: Annotated[detail, Query()]):
    return filter
