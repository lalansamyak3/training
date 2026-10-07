"""Many endpoints need the
same helper stuff: pagination params
, a DB session, the current user
, an API key check. Instead of repeating that code, you write it once as a dependency (a function). Then you say "this endpoint depends on that function", and FastAPI runs it for you
 and passes the result in."""

"""a dependency is a reusable function. 
You write it once, put Depends(...) in 
the route, and FastAPI calls it and gives 
you the result, so you don't repeat code
 or build things by hand in every route."""
from fastapi import Depends
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": min(limit, 100)}


@app.get("/books")
def list_books(page: Annotated[dict, Depends(pagination)]):
    return {"page": page}


@app.get("/authors")
def list_authors(page: Annotated[dict, Depends(pagination)]):
    return {"page": page}


"""here we creeate the pagination function 
which can be reused by the other routes
"""
