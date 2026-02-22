from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


DB_URL = "postgresql://postgres:01031990@localhost/bookingFastAPI"
engine = create_engine(DB_URL)


SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()