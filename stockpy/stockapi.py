from __future__ import annotations
from .constants import *
from .errors import *
import requests
import time


class StockAPI:

    def __init__(self, key: str) -> None:
        if self.validKeyFormat(key):
            self.key = key
        else:
            raise BadKeyFormat('The key format is invalid.')

        self.url = 'https://tomdanilov.pythonanywhere.com/api'
        self.keyargument = f'?key={self.key}'

        self.last_request = None
        self.show_errors = True

        if not self.isAlive():
            raise NotAlive('API is not alive or your key is invalid.')

    def validKeyFormat(self, key: str) -> bool:
        if False in [x.isnumeric() or x.isalpha() for x in key]:
            return False

        if len(key) != VALID_KEY_LENGTH:
            return False

        return True

    def isAlive(self) -> bool:
        if self.last_request:
            if not time.time() > (self.last_request + 2):
                time.sleep(time.time() - self.last_request)

        url = f'{self.url}{self.keyargument}'
        response = requests.get(url).json()

        if 'error' in response:
            self.showError(response)
            return False
        else:
            self.updateLastRequest()
            return response['alive']

    def search(self, query: str) -> dict:
        if self.last_request:
            if not time.time() > (self.last_request + 2):
                time.sleep(time.time() - self.last_request)

        url = f'{self.url}{self.keyargument}/stock/search&query={query}'
        response = requests.get(url).json()

        if 'error' in response:
            self.showError(response)
            return False
        else:
            self.updateLastRequest()
            return response

    def price(self, symbol: str) -> dict:
        if self.last_request:
            if not time.time() > (self.last_request + 2):
                time.sleep((time.time() + 2) - self.last_request)

        url = f'{self.url}/stock/price{self.keyargument}&symbol={symbol}'
        response = requests.get(url).json()

        if 'error' in response:
            self.showError(response)
            return False
        else:
            self.updateLastRequest()
            return response

    def updateLastRequest(self) -> None:
        self.last_request = time.time()

    def showError(self, response: dict) -> None:
        if self.show_errors:
            print('error', response['error'])
