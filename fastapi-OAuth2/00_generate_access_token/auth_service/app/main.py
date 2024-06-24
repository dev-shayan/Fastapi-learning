from fastapi import FastAPI
from jose import JWTError, jwt
from datetime import datetime, timedelta,timezone
from typing import Annotated
app = FastAPI()

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
    token=create_access_token(username,expiry_date)
    return {"token":token}

@app.get("/decode")
def decoding_token(token:str):
    try:
        decoded_token=decode_token(token)
        return {"Decoded Access Token":decoded_token}
    except JWTError as e:
        return{"Error":str(e)}