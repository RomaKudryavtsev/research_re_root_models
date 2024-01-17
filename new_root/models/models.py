import inspect
from sqlalchemy import Column, String, BigInteger

from new_root.models.database import Base

class User(Base):
    __tablename__ = "User"
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String)
    first_name = Column(String)