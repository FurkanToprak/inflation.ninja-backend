import requests
import os

def getWatchList(): # TODO: get 1000 top stocks by volume
    return ["IBM", "AAPL"]

def fetchStock(ticker):
    ALPHA_VANTAGE_SECRET = os.getenv('ALPHA_VANTAGE_SECRET')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_SECRET}'
    fetchedData = requests.get(url)
    fetchedJson = fetchedData.json()
    timeSeries = fetchedJson['Time Series (Daily)']
    return timeSeries

def fetchTopTradedStocks(): # TODO:
    return {
        'IBM': {}
    }