from fastapi import status

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


#######################################################################################
import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

FILE = Path("hero.json")


# ---------- Schemas ----------
class HeroCreate(BaseModel):
    name: str
    age: int
    gender: str
    marks: int
    password: str


class HeroRead(BaseModel):  # password is NOT here
    id: int
    name: str
    age: int
    gender: str
    marks: int


class HeroUpdate(BaseModel):  # PUT: all fields required
    name: str
    age: int
    gender: str
    marks: int
    password: str


class HeroPatch(BaseModel):  # PATCH: all fields optional
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    marks: Optional[int] = None
    password: Optional[str] = None


# ---------- File helpers ----------
def load_heroes() -> list[dict]:
    if not FILE.exists():
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_heroes(heroes: list[dict]) -> None:
    with open(FILE, "w") as f:
        json.dump(heroes, f, indent=2)


def find_hero(heroes: list[dict], hero_id: int) -> Optional[dict]:
    for hero in heroes:
        if hero["id"] == hero_id:
            return hero
    return None


# ---------- CREATE (201) ----------
@app.post("/heroes", status_code=status.HTTP_201_CREATED, response_model=HeroRead)
def create_hero(hero: HeroCreate):
    heroes = load_heroes()
    new_id = max((h["id"] for h in heroes), default=0) + 1
    new_hero = {"id": new_id, **hero.model_dump()}
    heroes.append(new_hero)
    save_heroes(heroes)
    return new_hero


# ---------- READ ALL (200) ----------
@app.get("/heroes", response_model=list[HeroRead])
def list_heroes():
    return load_heroes()


# ---------- READ ONE (200 / 404) ----------
@app.get("/heroes/{hero_id}", response_model=HeroRead)
def get_hero(hero_id: int):
    hero = find_hero(load_heroes(), hero_id)
    if hero is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found"
        )
    return hero


# ---------- PUT: replace everything (200 / 404) ----------
@app.put("/heroes/{hero_id}", response_model=HeroRead)
def replace_hero(hero_id: int, data: HeroUpdate):
    heroes = load_heroes()
    hero = find_hero(heroes, hero_id)
    if hero is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found"
        )
    hero.update(data.model_dump())
    save_heroes(heroes)
    return hero


# ---------- PATCH: update only sent fields (200 / 404) ----------
@app.patch("/heroes/{hero_id}", response_model=HeroRead)
def patch_hero(hero_id: int, data: HeroPatch):
    heroes = load_heroes()
    hero = find_hero(heroes, hero_id)
    if hero is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found"
        )
    hero.update(data.model_dump(exclude_unset=True))  # only fields the client sent
    save_heroes(heroes)
    return hero


# ---------- DELETE (204 / 404) ----------
@app.delete("/heroes/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hero(hero_id: int):
    heroes = load_heroes()
    hero = find_hero(heroes, hero_id)
    if hero is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found"
        )
    heroes.remove(hero)
    save_heroes(heroes)
    # return nothing
