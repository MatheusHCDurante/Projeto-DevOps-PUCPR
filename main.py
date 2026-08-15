from fastapi import FastAPI
import random

app = FastAPI()
# 217.0.0.1:8000/

@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def root():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}