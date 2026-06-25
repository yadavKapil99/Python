from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Welcome to the Home Page!", "status": "success", "code": 200, "data":["kapil", "sachin", "rohit"]} 