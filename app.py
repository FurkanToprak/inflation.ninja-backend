from dotenv import load_dotenv
from flask import Flask
import os
import logging
from stock_cache import StockCache
from stock import fetchStock

load_dotenv()

flaskApp = Flask(__name__)
appPort = os.getenv('APP_PORT')

stockCache = StockCache()
if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=appPort, debug=True)

@flaskApp.route("/getTopStocks", methods=["POST"])
def getTopStocks():
    # TODO: cache
    return {
        'top': []
    }

@flaskApp.route("/getStock", methods=["POST"])
def getStock():
    # TODO: query + cache
    return {}