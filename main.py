from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class ItemNotFoundException(HTTPException):
    def __init__(self, item_id: int):
        self.item_id = item_id
        
@app.exception_handler(ItemNotFoundException)
def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Item with ID {exc.item_id} not found.", "status": "error"},
    )

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id != 1:
        raise ItemNotFoundException(item_id)

    return {"message": "Item found", "item_id": item_id}
