from fastapi import FastAPI

app = FastAPI()  # instantiate FastAPI program

# API node
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello world"}


@app.get("/home")
async def home() -> dict:
    return {"message": "welcome home"}
