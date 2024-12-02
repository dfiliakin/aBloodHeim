from sqlalchemy import Column, Integer, String

from ..db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)

    # FIXME: Store hashed passwords
    password = Column(String(200), nullable=False)
