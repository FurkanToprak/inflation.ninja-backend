from stock import fetchStock

class StockCache:
    def __init__(self):
        self._cache = {}
        # TODO: create workers that run daily to update stock values + update best returns
    
    def addEntry(self, ticker: str, timeSeries: dict) -> None:
        self._cache[ticker] = timeSeries

    def updateEntry(self, ticker: str, dayKey: str, dayValue: dict) -> None:
        staleEntry: dict = self._cache.get(ticker)
        staleEntry[dayKey] = dayValue
        self._cache[ticker] = staleEntry

    def clearEntry(self, ticker: str) -> None:
        self._cache.pop(ticker)
    
    def getEntry(self, ticker: str) -> dict | None:
        if ticker not in self._cache:
            freshEntry = fetchStock(ticker)
            self.addEntry(ticker, freshEntry)
        return self._cache.get(ticker)
    
    def getTopEntries(self, period: str) -> dict:
        # TODO: find and separate calcs by inflationary periods, timeframes, etc.
        return self._cache