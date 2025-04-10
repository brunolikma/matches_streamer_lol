import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

api_key = os.getenv('apikey')
puuid_minerva = os.getenv('puuid_minerva')




def id_match ():
    list_idPartida = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid_minerva}/ids?start=0&count=20&api_key={api_key}').json()
    return list_idPartida





if __name__ == '__main__':
    id_match = id_match()