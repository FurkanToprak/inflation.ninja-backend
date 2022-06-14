from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
import os
import logging
from stock_cache import StockCache
from api import fetchStock

logging.basicConfig(filename='log/app.log', level=logging.INFO)

app = Flask(__name__)
appPort = os.getenv('APP_PORT')

stockCache = StockCache()

@app.route('/', methods=["GET"])
def health():
    return 'Hello, World!'

@app.route("/getTopStocks", methods=["GET"])
def getTopStocks():
    return stockCache.getTopEntries()

@app.route("/getStock", methods=["GET"])
def getStock():
    """ 
    Gets daily data on a stock from the cache. 
    If not in cache, fetches from AlphaVantage API. 
    """
    ticker = request.args['ticker']
    return stockCache.getEntry(ticker)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=appPort)