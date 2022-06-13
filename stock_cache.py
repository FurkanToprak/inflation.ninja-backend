from time import sleep
from api import fetchStock, fetchCPI, getTopTradedList
from datetime import datetime
import logging

logging.basicConfig(filename='log/stock_cache.log', level=logging.INFO)
def marketIsOpen():
    # TODO: add holidays: https://www.nyse.com/markets/hours-calendars
    return datetime.today().weekday() < 5 # MTWTF are 0-4
 
def todayKey():
    return datetime.today().strftime('%Y-%m-%d')

class StockCache:
    def __init__(self):
        self._cache = {}
        self.requestQueue = []
    
    def addEntry(self, ticker: str, timeSeries: dict) -> None:
        self._cache[ticker] = timeSeries

    def clearEntry(self, ticker: str) -> None:
        self._cache.pop(ticker)
    
    def getEntry(self, ticker: str) -> dict | None:
        """ Gets stock/CPI and caches. """
        def refreshEntry():
            apiRetry = False
            while True:
                try:
                    freshEntry = fetchCPI() if ticker == "Inflation" else fetchStock(ticker) 
                    self.addEntry(ticker, freshEntry)
                    break
                except Exception as err:
                    if apiRetry:
                        logging.info('[Attempt 2] Failed to fetch fresh data. Aborting.')
                        return None
                    apiRetry = True
                    logging.info('[Attempt 1] Failed to fetch fresh data.')
                    logging.info(err)
                    sleep(60) # Likely API limit hit, wait minute.
        if ticker not in self._cache:
            refreshEntry()
        else:
            tickerData = self._cache.get(ticker)
            if marketIsOpen() and todayKey() not in tickerData:
                refreshEntry()

        return self._cache.get(ticker)
    
    def getTopEntries(self) -> dict:
        stockList = getTopTradedList()
        topStocks = dict()
        for stock in stockList:
            stockValue = self.getEntry(stock)
            topStocks[stock] = stockValue
        return topStocks