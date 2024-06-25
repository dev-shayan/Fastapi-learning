# ​‌‌‍Order Matters:​ The order of path parameters in the URL must match the function signature.<br>
#           ​‌‌‍Mapping:​ FastAPI maps the URL values to the function parameters based on their position in the URL.<br>
# ​‌‌‍   Consistency:​ Always ensure that the URL pattern and the function signature maintain a consistent order for path parameters.

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/items/{item_id}/users/{user_id}")
# def root( user_id: int,item_id: int):
#     return {"items": item_id, "users": user_id}

# The URL pattern /items/{item_id}/users/{user_id} has two path parameters: item_id and user_id.
# The function root has two parameters: user_id and item_id.
# FastAPI maps the URL values to the function parameters based on their position in the URL.
# The order of path parameters in the URL must match the function signature.
# The URL pattern and the function signature maintain a consistent order for path parameters.⁡


from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item, q: Annotated[str | None, Query(max_length=10, min_length=3)] = None):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    if q:
        item_dict.update({"q": q})
    print("items:", item_dict,)
    return {"items": item_dict,}
