from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float 


@app.get("/")
async def health_check():
    return {"message": "Hello World"}

@app.put("/items/{item_id}")
async def put_item(item_id: int , 
                    q: str | None = None,
                    item: Item = None):
    res = {"item_id": item_id, **item.dict()}
    if q:
        return {**res, "q": q}
    else :
        return res