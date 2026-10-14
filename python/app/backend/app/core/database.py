from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""from app.core.config import settings: imports the config you just saw, so the DB URL comes from .env.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True): creates the engine, which manages a pool of connections to PostgreSQL. pool_pre_ping=True tests a connection before using it, so stale or dropped connections (e.g. after a DB restart) are replaced instead of causing errors.
SessionLocal = sessionmaker(...): a factory that creates database sessions bound to that engine.
autoflush=False: pending changes aren’t sent to the DB automatically before queries; you control it with commit() or flush().
autocommit=False: nothing is saved until you explicitly call db.commit().
class Base(DeclarativeBase): the parent class for all your models. Each model (e.g. User) inherits from Base, and SQLAlchemy uses it to track tables and create them.

get_db()

This is a FastAPI dependency:

python
@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
It opens a new session, yields it to the route, then always closes it in finally, even if the route raises an error.
This gives one session per request and prevents connection leaks.

One thing to note: because autocommit=False, you need to call db.commit() after inserts or updates, or the changes will be lost when the session closes."""
