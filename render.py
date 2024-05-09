import json
import sqlite3
from databases import Database
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from t_bot.db import db_get_all_products

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

database = sqlite3.connect('database.db')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    result = database.execute("SELECT * FROM products").fetchall()
    products = []
    for product in result:
        products.append({"name": product[1], "price": product[3]})
    print(products)
    return templates.TemplateResponse("index.html", {"request": request, "products": products})
