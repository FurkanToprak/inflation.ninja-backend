class StockCache:
    def __init__(self):
        self._cache = {}
        # TODO: create workers that run daily to update stock values + update best returns
    
    def addEntry(self, ticker: str, timeSeries: dict):
        self._cache[ticker] = timeSeries

    def updateEntry(self, ticker: str, dayKey: str, dayValue: dict):
        staleEntry: dict = self._cache.get(ticker)
        staleEntry[dayKey] = dayValue
        self._cache[ticker] = staleEntry

    def clearEntry(self, ticker: str):
        self._cache.pop(ticker)