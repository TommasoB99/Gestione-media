#import json
#import requests

API = """https://www.googleapis.com/books/v1/volumes?q="""


def prepara_link(titolo):
    titolo = titolo.replace(' ', '+').lower()
    titolo = API + titolo
    return titolo

