
from fastapi import FastAPI

app = FastAPI()

@app.get("/echo/")
async def echo(name: str):
    return f"tu nombre es {name}"

