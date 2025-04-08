import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('apikey')
puuid_minerva = os.getenv('puuid_minerva')




def id_match ():
    url = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid_minerva}/ids?start=0&count=20&api_key={api_key}')
    print(url.json())