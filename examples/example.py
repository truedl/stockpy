# Example program to check stock price every 10 seconds
from __future__ import annotations
from stockpy import *
import datetime
import time


class PriceFormation:

    def __init__(self) -> None:
        self.previous = None
        self.changes = []

    def showPrice(self, data: dict) -> str:
        if self.previous:
            change = round(data['price'] - self.previous, 2)
            if change > 0:
                change = f'+{str(change)}'

            self.changes.append(str(change))

            self.updatePrevious(data)
            avg = eval('+'.join(self.changes))
            return f'{data["price"]} (CHANGE {change}, AVG {round(avg/len(self.changes), 3)})'

        else:
            self.updatePrevious(data)
            return str(data['price'])

    def updatePrevious(self, data: dict) -> None:
        self.previous = data['price']


if __name__ == '__main__':
    api = StockAPI(
        key = 'api_key'
    )

    priceGraphics = PriceFormation()
    stock = 'GOOGL'

    while True:
        price = api.price(stock)

        if price:
            print(
                f'[{str(datetime.datetime.now())}]',
                f'CURRENT "{stock}" STOCK PRICE IS',
                priceGraphics.showPrice(
                    price
                )
            )

        time.sleep(10)
