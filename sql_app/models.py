from sqlalchemy import Column, Integer, String
from sql_app.database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(500))
    fullname = Column(String(50), unique=True)


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(500))










