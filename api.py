# # pre requisite 
# pip install fastapi
# pip install uvicorn
# pip install requests
# pip install bs4

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/{asin}")
async def get_data(asin: str):
    return{"result": asin}