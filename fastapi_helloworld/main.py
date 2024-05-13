from enum import Enum
from fastapi import FastAPI, HTTPException


app = FastAPI()


# query parametrs
@app.get("/")
async def message2(message: str = "HELLO"):
    return message

    # example1 from docs of query parameters


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 1, limit: int = 10):
    return fake_items_db[skip : skip + limit]

    # example2 from docs of query parameters


# here item_id is path and q is query parameter adn fastapi is smart enough
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# example3 from docs of query parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False, q: str | None = None):
    items = {"item_id": item_id}
    if short:
        items.update({"short": short})
        print("added short in items")
    if q:
        items.update({"q": q})
        print("added q in items")
    return items


# path parametr
@app.get("/{user}")
async def get_model(user: str):
    return f"Hello {user} from path paramters"
