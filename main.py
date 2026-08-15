# 217.0.0.1:8000/
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 217.0.0.1:8000/teste
@app.get("/teste1")
async def root():
    return {"teste": "deu certo"}