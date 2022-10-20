from .database import *
import json
import datetime

#import requests

API = """https://www.googleapis.com/books/v1/volumes?q="""


def prepara_link(titolo):
    titolo = titolo.replace(' ', '+').lower()
    titolo = API + titolo
    return titolo

def esporta_database(data):
    x = datetime.datetime.now()
    with open("data/database_"+x.strftime("%Y%m%d") +".json", 'w') as f:
        json.dump(data, f, indent=4)


    

