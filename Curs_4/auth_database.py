from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the MySQL database
DATABASE_URL = "mssql+pyodbc://DESKTOP-3SK5E6S/school?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

# Setup database
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(150), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

