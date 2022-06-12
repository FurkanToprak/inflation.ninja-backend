from dotenv import load_dotenv
from flask import Flask
import requests
import os

load_dotenv()

flaskApp = Flask(__name__)
appPort = os.getenv('STOCK_API_SECRET')
appPort = os.getenv('APP_PORT')

if __name__ == '__main__':
    # TODO: initialize cache and calculations
    flaskApp.run(host='0.0.0.0', port=appPort, debug=True)

def initCache():
    pass

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