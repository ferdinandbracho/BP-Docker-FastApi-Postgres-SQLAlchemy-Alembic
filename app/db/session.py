from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://traxi:traxi@localhost:5432/traxi_fleet')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()