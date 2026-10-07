from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


from uuid import UUID


@app.get("/order/{order_id}")
def get_order(order_id: UUID):
    return {"order_id": order_id}


from typing import Annotated

from fastapi import Path


@app.get("/userss/{user_id}")
def get_items(
    user_id: Annotated[
        int, Path(title="item_id", desription="the id is here ", ge=100, le=1000)
    ],
):
    return {"user_id": user_id}


from enum import Enum


class Role(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"


@app.get("/role/{role}")
def get_role(role: Role):
    if role is Role.admin:
        return {"role": role, "access": "everything "}
    return {"role": role.value, "access": "limited"}


"""static part of url befor dynamic otherise it will take the poart as useroid
"""
