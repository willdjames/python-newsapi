# api_google.py
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
import os
import json

class ApiGoogleNoticias:

    def __init__(self):
        api_key = os.getenv('NEWSAPI_KEY')
        self.__newsapi = NewsApiClient(api_key=api_key)

    
    def get_noticias_relevantes(self):
        try:
            return self.__newsapi.get_top_headlines(country='br')
        except NewsAPIException as e:
            print(e)
            raise Exception(e.get_code())