# main.py
from fastapi import FastAPI, HTTPException
import json
from integracao.api_google import ApiGoogleNoticias

app = FastAPI()


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
    try:
        return ApiGoogleNoticias().get_noticias_relevantes()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.args[0])