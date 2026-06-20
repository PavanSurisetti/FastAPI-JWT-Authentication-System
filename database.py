#this file contains database connections and creation of  sessions
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
load_dotenv()#loading .env
DATABASE_URL=os.getenv('DATABASE_URL')
#creating base class for all tables
Base=declarative_base()
#engine creation
engine=create_engine(DATABASE_URL)
#session creation
SessionLocal=sessionmaker(bind=engine)