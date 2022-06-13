from stock import fetchStock
from datetime import datetime

def marketIsOpen():
    # TODO: add holidays: https://www.nyse.com/markets/hours-calendars
    return datetime.today().weekday() < 5 # MTWTF are 0-4
 
def todayKey():
    return datetime.today().strftime('%Y-%m-%d')

class StockCache:
    def __init__(self):
        self._cache = {}
        # TODO: create workers that run daily to update stock values + update best returns

    def clearEntry(self, ticker: str) -> None:
        self._cache.pop(ticker)
    
    def getEntry(self, ticker: str) -> dict | None:
        def refreshEntry():
            freshEntry = fetchStock(ticker)
            self.addEntry(ticker, freshEntry)

        if ticker not in self._cache:
            refreshEntry()
        else:
            tickerData = self._cache.get(ticker)
            if marketIsOpen() and todayKey() not in tickerData:
                refreshEntry()

        return self._cache.get(ticker)
    
    def getTopEntries(self, period: str) -> dict:
        # TODO: find and separate calcs by inflationary periods, timeframes, etc.
        return self._cache