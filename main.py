# 217.0.0.1:8000/
from fastapi import FastAPI

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def root():
    return {"teste": "deu certo"}