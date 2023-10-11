from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hail": "Zorp"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id}

