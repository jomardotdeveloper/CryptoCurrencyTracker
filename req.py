import requests


class CoinGeckoAPI:
    def __init__(self):
        self.coin_list_url = 'https://api.coingecko.com/api/v3/coins/list'
        self.currency_list_url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'
        self.price_url = 'https://api.coingecko.com/api/v3/simple/price'

    def get_coin_list(self):
        req_api = requests.get(self.coin_list_url)
        return req_api.json()

    def get_currency_list(self):
        req_api = requests.get(self.currency_list_url)
        return req_api.json()

    def get_price(self, coin_id, currency):
        req_api = requests.get(self.price_url, params={
                               'ids': coin_id, 'vs_currencies': currency})
        return req_api.json()
