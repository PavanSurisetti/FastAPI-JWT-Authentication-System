#this file contains all the API endpoints 
from fastapi import FastAPI,Depends,HTTPException#to create application and helps to reuse the code using dependency function,to raise http exception also
from pydantic import BaseModel#this is used for data validation
from database import Base,engine,SessionLocal#used to create all the tables in the database and also connect to database locally
from sqlalchemy.orm import Session#for session
import models#this is to access the table
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from passlib.context import CryptContext #for security
oauth2Scheme=OAuth2PasswordBearer(tokenUrl='login')
pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
load_dotenv()
#for jose library
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
#--create all tables--
Base.metadata.create_all(engine)
#--create fastapi app--
app=FastAPI()
#create dependency function to reuse the logic
def get_db():
    db=SessionLocal()
    try:
        yield db#this is used to give db to api
    finally:
        db.close()
class register_user(BaseModel):#to validate the data
    username:str
    email:str
    password:str
def hashpassword(password:str):
    return (pwd_context.hash(password))
def verifyPassword(plainpassword:str,hashpassword):
    return (pwd_context.verify(plainpassword,hashpassword))
@app.get('/',tags=['Welcome'])
def home():
    return 'Welcome to Authentication System'
#---Register User---
@app.post('/register',tags=['Create User'])
def create_user(*,db:Session=Depends(get_db),add:register_user):
    user=models.user(name=add.username,email=add.email,password=hashpassword(add.password))
    #hashpassword will return the hashed version of the password
    db.add(user)#this will add the user to session
    db.commit()#this will permanently saves the details in the database
    db.refresh(user)
    return{
        'message':'User Created Successfully',
        'user':{
            'id':user.id,
            'Name':add.username,
            'email':add.email
        }
    }
#--creating a function for token generation---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#---creating a function for token validation
def verify_token(token:str):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401,detail='Invalid Token or Token Expired')
#---Login User---
@app.post('/login',tags=['Login'])
def loginUser(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    if not verifyPassword(form_data.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token({"sub": str(user.id)})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user.name
    }
#to get current user
def get_current_user(token:str=Depends(oauth2Scheme)):
    payload=verify_token(token)
    return int(payload.get('sub'))
@app.get('/profile',tags=['Get Profile'])
def get_profile(user=Depends(get_current_user),db:Session=Depends(get_db)):
    userdetails=db.query(models.user).filter(models.user.id==user).first()
    if userdetails:
        return{
        'id':userdetails.id,
        'name':userdetails.name,
        'email':userdetails.email
                }
    raise HTTPException(status_code=404,detail='user not found')