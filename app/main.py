from fastapi import FastAPI
from .utils import add

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add_api(a: int, b: int):
    return {"result": add(a, b)}
