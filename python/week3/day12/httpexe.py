from fastapi import FastAPI, HTTPException
from pdantic import BaseModel
from pydantic import Annotated, Field

app = FastAPI()

users = [
    {"id": 1, "name": "samyak", "age": 21},
    {"id": 2, "name": "sa", "age": 23},
    {"id": 3, "name": "sk", "age": 25},
    {"id": 4, "name": "yak", "age": 26},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="usernot found")
    return users[user_id]
