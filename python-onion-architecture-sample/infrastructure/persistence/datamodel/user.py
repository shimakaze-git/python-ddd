from sqlalchemy import Column, Integer, String, Text, DATETIME
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from datetime import datetime
Base = declarative_base()


class Users(Base):
    """テーブルの定義"""
    __tablename__ = 'users'

    id = Column('id', Integer(unsigned=True), primary_key=True, autoincrement=True)
    name = Column('name', String(255), index=True, unique=True)
    created_at = Column('created_at', DATETIME, default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DATETIME, default=datetime.now, nullable=False)

    def __init__(self, name, age):
        self.name = name

        now = datetime.now()
        self.created_at = now
        self.updated_at = now
