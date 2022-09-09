"""
Created an API that:

1. Receives HTTP requests in the paths / and /items/{item_id}.
2. Both paths take GET operations (also known as HTTP methods).
3. The path /items/{item_id} has a path parameter item_id that should be an int.
4. The path /items/{item_id} has an optional str query parameter q.

"""

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

