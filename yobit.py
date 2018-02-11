import requests
import json

def get_liza():
    #url = 'https://yobit.net/api/2/btc_usd/ticker'
    url = 'https://yobit.net/api/2/liza_rur/ticker/'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(price) + ' рублей'
