from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float 


@app.get("/")
async def health_check():
    return {"message": "Hello World"}


@app.put("/items/{item_id}")
async def put_item(item_id: Annotated[int, Path(ge=1, le=1000)], 
                    q: Annotated[str|None, Query(max_length=50, min_length=3)] = None,
                    item: Item = None):
    res = {"item_id": item_id, **item.dict()}
    if q:
        return {**res, "q": q}
    else :
        return res

@app.get("/items/{item_id}")
async def get_item(
    item_id: Annotated[int, Path(ge=1, le=1000)], 
    q: Annotated[str|None, Query(max_length=50, min_length=3)] = None, 
    sort_order: SortOrder = SortOrder.asc):
    if q:
        return {
            "item_id": item_id, 
            "description": "This is a sample item that matches the query test_query",
            "sort_order": sort_order
        }
    else:
        return {
            "item_id": item_id,
            "description": "This is a sample item.",
            "sort_order": sort_order
        }
    return {"item_id": item_id, "q": q}