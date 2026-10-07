from sqlalchemy import select
from python.week2.day10.db import SessionLocal
from models import User, Post

# --- CREATE ---
with SessionLocal() as session:
    alice = User(name="Alice", email="alice@example.com")
    alice.posts.append(Post(title="Hello", body="My first post"))
    alice.posts.append(Post(title="Second", body=None))
    session.add(alice)  # only stages it; posts come along via the relationship
    session.commit()  # writes to the DB

# --- READ ---
with SessionLocal() as session:
    user = session.scalars(select(User).where(User.email == "alice@example.com")).one()
    print(user.name, [p.title for p in user.posts])  # relationship in action

    all_users = session.scalars(select(User).order_by(User.name)).all()
    first_or_none = session.scalars(select(User).where(User.id == 999)).first()

# --- UPDATE ---
with SessionLocal() as session:
    user = session.get(User, 1)  # fetch by primary key
    user.name = "Alice Smith"  # just change the attribute
    session.commit()  # ORM notices the change and issues UPDATE

# --- DELETE ---
with SessionLocal() as session:
    user = session.get(User, 1)
    session.delete(user)  # cascade deletes their posts too
    session.commit()

# --- ERRORS ---
with SessionLocal() as session:
    try:
        session.add(User(name="Bob", email="dup@example.com"))
        session.add(User(name="Bob2", email="dup@example.com"))  # unique violation
        session.commit()
    except Exception:
        session.rollback()  # undo everything since the last commit
        raise
