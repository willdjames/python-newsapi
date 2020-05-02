# main.py
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.get('/hello')
def get_hello_world():
    return {"hello" : "world"}


@app.get('/noticias/mock'
,responses={200:{}
            ,404:{"description":"Mock não encontrado"}}
)
def noticias_mock():
    try:
        with open('response_mock.json', 'r') as json_mock:
            return json.load(json_mock)
    except:
        raise HTTPException(status_code=404, detail='Mock não encontrado')