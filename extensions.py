import json
import requests
from config import keys


class ConvertionExceptions(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExceptions(f"Не удалось перевести одинаковые валюты {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExceptions(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExceptions(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceptions(f"Не удалось обработать количество {amount}")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
