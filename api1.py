from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/{asin}")
async def get_data(asin: str):
    session = requests.Session()
    session.headers.update({
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    # we created f string, which means we are pssing the variable into this amazon url
    resp = session.get(f"https://amazon.in/dp/{asin}")

    # create a soup to pass the html informatin 
    soup= BeautifulSoup(resp.text, "html.parser")

    # construct the response that we want to make
    data = {
        "asin": asin,
        "name": soup.select_one("h1#title").text.strip(),
        "price": soup.select_one("span.a-offscreen").text,
    }

    return{"result": data}