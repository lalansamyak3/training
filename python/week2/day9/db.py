from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///app.db", echo=True)  # echo=True prints the SQL
SessionLocal = sessionmaker(engine)
