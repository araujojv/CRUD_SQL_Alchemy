from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column

class Base(DeclarativeBase):
    pass
