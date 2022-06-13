from api import fetchStock, fetchCPI
from datetime import datetime
import logging

logging.basicConfig('log/stock_cache.log', level=logging.INFO)
def marketIsOpen():
    # TODO: add holidays: https://www.nyse.com/markets/hours-calendars
    return datetime.today().weekday() < 5 # MTWTF are 0-4
 
def todayKey():
    return datetime.today().strftime('%Y-%m-%d')

class StockCache:
    def __init__(self):
        self._cache = {}
        
        # TODO: create workers that run daily to update top stocks + returns over intervals
    
    def addEntry(self, ticker: str, timeSeries: dict) -> None:
        self._cache[ticker] = timeSeries

    def clearEntry(self, ticker: str) -> None:
        self._cache.pop(ticker)
    
    def getEntry(self, ticker: str) -> dict | None:
        """ Gets stock/CPI and caches. """
        def refreshEntry():
            try:
                freshEntry = fetchCPI() if ticker == "Inflation" else fetchStock(ticker) 
                self.addEntry(ticker, freshEntry) # TODO: if fails, just skip
            except Exception as err:
                logging.info('Failed to fetch fresh data.')
                logging.info(err)
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