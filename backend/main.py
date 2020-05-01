# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
def get_hello_world():
    return {"hello" : "world"}