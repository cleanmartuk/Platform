from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv
load_dotenv()


evn_x_token = pword = os.getenv('x_token')
evn_token = pword = os.getenv('token')


async def get_token_header(x_token: str = Header(...)):
    if x_token != evn_x_token:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != evn_token:
        raise HTTPException(status_code=400, detail="No Jessica token provided")