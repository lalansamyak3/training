from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

"""tllls sqlalchemy where to connect """

"""test.db is the database file that will be created in the current directory."""

"""only chalenge to shift to pstgre is changing this url only """

"""rest of the code remain same """

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

"""sqllite only allow one tgread but fastapi allow multiple request  across thread so we diable the restriction"""

"""sessionmaker is a factory for creating new Session objects. It is used to manage database connections and transactions."""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""session is essentially a transaction with the db

each request gets its own session we make auto commit as false and auto flush as false we will control when changes are commited """

"""DeclarativeBase is a base class for defining SQLAlchemy models using the declarative syntax. It provides a convenient way to define database tables and their relationships."""


class Base(DeclarativeBase):

    pass


"""get_db is a function that creates a new database session and yields it. It is used as a dependency in FastAPI routes to provide access to the database."""

"""with the with statement make the session as the context manager kind of like opening the file """

"""yoields ensure the cleaup even if the eror occurs """

"""fastapi depemndency injection call this function for each request and handle the cleanup automatically"""


def get_db():

    with SessionLocal() as db:

        yield db
