import requests
import os

ALPHA_VANTAGE_SECRET = os.getenv('ALPHA_VANTAGE_SECRET')

def getWatchList(): # TODO: get 1000 top stocks by volume
    return ["IBM", "AAPL"]

def fetchStock(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_SECRET}'
    fetchedData = requests.get(url)
    fetchedJson = fetchedData.json()
    timeSeries = fetchedJson['Time Series (Daily)']
    return timeSeries

def fetchCPI() -> dict:
    """
    Returns { "date": "YYYY-MM-DD", "value": "x.y" }[]
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
