'''
This class handles all the data retrieval and standardizes the data for all technical analyses
'''

import websocket
import requests
import json  # For web connectivity
from abc import ABC, abstractmethod  # Abstract class module for python.
import alpaca_trade_api as tradeapi
from dataclasses import dataclass  # Python structs module.
import pandas as pd  # For data storage and analysis.
import ast, datetime # For on_message data handling

class DataHandler:
    
    def __init__(self, api_key, secret_key, base_url, socket=""):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url 
        self.headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key
        }
        self.api = tradeapi.REST(self.headers["APCA-API-KEY-ID"],
                                 self.headers["APCA-API-SECRET-KEY"], base_url)
        self.ws = None
        self.socket = socket
        self.pending_tickers = []

    """
        Overview: Returns the data handler object's socket
    """
    def getSocket(self):
        return self.ws
    
    """
        Overview: Returns a dataframe of stock data of a particular ticker 

        Parameters:
            - ticker
            - start_time
            - end_time
            - bar_timeframe
            - bar_limit
        
        Returns:
            - (dataframe) stock data of a particular ticker 
    """
    def getBars(self, ticker: str, _start_time: str, _end_time: str, bar_timeframe: str, bar_limit: str):
        start_time = datetime.datetime.fromtimestamp(_start_time.time()).strftime('%Y-%m-%dT%H:%M:%S')
        end_time = datetime.datetime.fromtimestamp(_end_time).strftime('%Y-%m-%dT%H:%M:%S')
        url ='https://data.alpaca.markets/v2/stocks'+'/'+ticker+'/bars?adjustment=raw'+'&start='+start_time+'&end='+end_time+'&limit='+bar_limit+'&page_token='+'&timeframe='+bar_timeframe
        r = requests.get(url, headers=self.headers)
        df = pd.read_json(json.dumps(r.json()['bars']))
        df['oi'] = -1
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Open Interest']
        return df
    
    """
        Overview: receives the data bars as a df, then extracts and return the specific candle choice of data

        Parameters:
            - ticker
            - current_time
            - bar_timeframe
            - bar_limit
            - candle_choice 
        
        Returns:
            - data: (List) data of a particular candle choice 
    """
    def getData(self, ticker, current_time, bar_timeframe, bar_limit, candle_choice):
        start_time = current_time - bar_limit
        data_df = self.getBars(ticker, start_time, current_time, bar_timeframe, bar_limit)
        data = data_df[candle_choice] 
        return data 