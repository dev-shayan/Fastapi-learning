from fastapi import FastAPI,Depends,HTTPException,status
from jose import JWTError, jwt
from datetime import datetime, timedelta,timezone
from typing import Annotated,Optional
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

users_db: dict[str, dict[str, str]] = {
    "ameenalam1": {
        "username": "ameenalam",
        "full_name": "Ameen Alam",
        "email": "ameenalam@example.com",
        "password": "ameenalamsecret",
    },
    "mjunaid": {
        "username": "junaid",
        "full_name": "Muhammad Junaid",
        "email": "mjunaid@example.com",
        "password": "mjunaid",
    },}

ALGORITHM = "HS256"
SECRET_KEY="secret"

def create_access_token(subject:str,expire_delta:timedelta):
    expire= datetime.now(timezone.utc) + expire_delta
    to_encode={"sub":str(subject),"exp":expire}
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token:str):
    token_data=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    return token_data

app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/token")
def get_token(username:str):
    expiry_date=timedelta(minutes=1)
    token=create_access_token( username ,expiry_date)
    return {"username":username, "token":token}

@app.get("/decode")
def decoding_token(token:str):
    try:
        decoded_token=decode_token(token)
        return {"Decoded Access Token":decoded_token}
    except JWTError as e:
        return{"Error":str(e)}
@app.post("/login")
def login(data_from_user:Annotated[OAuth2PasswordRequestForm,Depends(OAuth2PasswordRequestForm)]):
   # Step1: Check if the username exists in users_db
    user_in_users_db = None
    for user in users_db.values():
        if user["username"] == data_from_user.username:
            user_in_users_db = user
            
    if user_in_users_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Username")
    # Step2: Verify the password
    if user_in_users_db["password"] != data_from_user.password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password")
    #step3: Create and return the access token
    expiry_date=timedelta(minutes=1)
    token=create_access_token(data_from_user.username,expiry_date)
    return {"username":data_from_user.username, "token":token}
@app.get("/all_users")
def get_all_users():
    return users_db
