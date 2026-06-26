from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    mock_user = User(
        id=user_id, name="John Doe", email="kapil@gmail.com", password="securepassword"
    )
    return mock_user


@app.post(
    "/create_user", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def create_user(user: User):
    return {"message": "User created successfully"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item found", "item_id": item_id}
