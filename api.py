import requests
import os

ALPHA_VANTAGE_SECRET = os.getenv('ALPHA_VANTAGE_SECRET')

def getWatchList(): # TODO: get 1000 top stocks by volume
    return ["IBM", "AAPL"]

def fetchStock(ticker):
    """
    Returns {
        "YYYY-MM-DD": {
        "1. open": X.Y,
        "2. high": X.Y,
        "3. low": X.Y,
        "4. close": X.Y,
        "5. volume": X.Y
    },
    }
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_SECRET}'
    fetchedData = requests.get(url)
    fetchedJson = fetchedData.json()
    timeSeries = fetchedJson['Time Series (Daily)']
    stock = dict()
    for day in timeSeries.keys():
        datum = timeSeries[day]
        highValue = float(datum["2. high"])
        lowValue = float(datum["3. low"])
        volumeValue = int(datum["5. volume"])
        stock[day] = {
            'high': highValue,
            'low': lowValue,
            'volume': volumeValue,
        }
    return stock

def fetchCPI() -> dict:
    """
    Returns { "YYYY-MM-DD": X.Y }
    """
    url = f'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey={ALPHA_VANTAGE_SECRET}'
    fetchedData = requests.get(url)
    fetchedJson = fetchedData.json()
    cpi = dict()
    for datum in fetchedJson['data']:
        key = datum['date']
        value = datum['value']
        cpi[key] = float(value)
    return cpi

def fetchTopTradedStocks(): # TODO:
    return {
        'IBM': {}
    }
