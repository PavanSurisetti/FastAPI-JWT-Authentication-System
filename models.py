#this files contains all the models that we use in the AUTHENTICATION SYSTEM
from database import Base
from sqlalchemy import Column,Integer,String
#creating model for user
class user(Base):
    __tablename__='Users'
    id=Column(Integer,primary_key=True)#id of the user which is unique
    name=Column(String,nullable=False)#name of user cannot be false
    email=Column(String,unique=True,nullable=False)#email of the user which is unique
    password=Column(String,nullable=False)#password cannot be null