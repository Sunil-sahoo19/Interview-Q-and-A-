#Q1. #Basics Hello World! code ?

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


#Q2. What is Quary parameter ?

from fastapi import FastAPI
app = FastAPI()

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

#Q3. What is Path parameter with validation ?

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

#Q4. post endponit with pydantic ?

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None 

 # POST endpoint using the model
@app.post("/items/")
async def create_item(item: Item):
    # Business logic: compute price with tax
    total_price = item.price + (item.tax if item.tax else 0)
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
        "total_price": total_price
    }

#Q5. complete CRUD operations ? 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

# In-memory "database"
items: List[Item] = []

# CREATE
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    # Check if item with same id exists
    for existing in items:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items.append(item)
    return item

# READ (all items)
@app.get("/items/", response_model=List[Item])
async def read_items():
    return items

# READ (single item by id)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")













