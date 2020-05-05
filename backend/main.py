# main.py
from fastapi import FastAPI, HTTPException
from newsapi import NewsApiClient
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


@app.get('/noticias'
        ,responses={200:{}}
)
def noticias_br():
    '''
    Top notícias do Brasil
    '''
    newsapi = NewsApiClient(api_key='dd65faf4401a4b8191d81de5d622de1c')

    return newsapi.get_top_headlines(country='br')
