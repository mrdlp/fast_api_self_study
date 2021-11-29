from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:cuong1990@localhost:3306/restapi" #original code
SQLALCHEMY_DATABASE_URL = "mysql://root:root@db/main" # for running inside docker
#SQLALCHEMY_DATABASE_URL = "mysql://root:root@127.0.0.1:33066/main" # for running in venv

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()





