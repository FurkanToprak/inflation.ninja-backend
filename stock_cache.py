from time import sleep
from api import fetchStock, fetchCPI, getTopTradedList
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='log/stock_cache.log', level=logging.DEBUG)

def getYesterday():
    return datetime.today() - timedelta(days=1)

def marketWasOpenYesterday():
    # TODO: add holidays: https://www.nyse.com/markets/hours-calendars
    return getYesterday().weekday() < 5 # MTWTF are 0-4
 
def yesterdayKey():
    return getYesterday().strftime('%Y-%m-%d')

class StockCache:
    def __init__(self):
        self._cache = {}
        # populate cache w top entries
        logging.debug('Cache initialization started.')
        self.getTopEntries()
        logging.debug('Cache initialization done.')
    
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
                    logging.debug(f'[getEntry] Successfully fetched ${ticker}')
                    break
                except Exception as err:
                    if apiRetry:
                        logging.info('[getEntry | Attempt 2] Failed to fetch fresh data. Aborting.')
                        return None
                    apiRetry = True
                    logging.info('[getEntry | Attempt 1] Failed to fetch fresh data.')
                    logging.info(err)
                    sleep(60) # Likely API limit hit, wait minute.
        if ticker not in self._cache:
            logging.debug(f'[getEntry] ${ticker} not cached.')
            refreshEntry()
        else:
            tickerData = self._cache.get(ticker)
            if marketWasOpenYesterday() and yesterdayKey() not in tickerData:
                logging.debug(f'[getEntry] ${ticker} cached but not fresh.')
                refreshEntry()
            else:
                logging.debug(f'[getEntry] ${ticker} cached and fresh.')


        return self._cache.get(ticker)
    
    def getTopEntries(self) -> dict:
        stockList = getTopTradedList()
        topStocks = dict()
        for stock in stockList:
            stockValue = self.getEntry(stock)
            topStocks[stock] = stockValue
        return topStocks