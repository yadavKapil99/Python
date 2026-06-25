from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def get_home():
    return {"message": "Welcome to the Home Page!", "status": "success", "code": 200, "data":["kapil", "sachin", "rohit"]} 


# -----------------------------------Query Parameters and Path Parameters-----------------------------------
# Path Parameters
# User Routes
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"message": f"User with ID {user_id} retrieved!", "status": "success", "code": 200, "data": {"id": user_id, "name": f"User {user_id}"}}
    # f" is to format it in string 
    
    
# Query Parameters
@app.get("/search")
def search_items(q: str, limit: int = 10, offset: int = 0):
    return {"message": f"Searching for items containing '{q}'!", "status": "success", "code": 200, "data": [{"name": f"Item {i}", "description": f"This is item {i}"} for i in range(limit)]}

# -----------------------------------Request Body-----------------------------------
@app.post("/items")
def create_item(item: dict, age: int):
    return {"message": "Item created successfully!", "status": "success", "code": 201, "data": {**item, "age": age}}


# -----------------------------------Request Body with Pydantic Models-----------------------------------
from pydantic import BaseModel

class User(BaseModel):
    name: str
    description: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message": "User created successfully!", "status": "success", "code": 201, "data": user}

# -----------------------------------Nested Models in Pydantic Models-----------------------------------
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    
class Item(BaseModel):
    name: str
    description: str
    age: int
    address: Address
    
@app.post("/item")
def create_item_with_address(item: Item):
    return {"message": "Item with address created successfully!", "status": "success", "code": 201, "data": item}