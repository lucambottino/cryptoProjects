import urllib.request
import ssl
import json
import time
import pandas as pd
from datetime import datetime
import numpy as np
import plotly
import ffn
import finquant
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from datetime import date
#import streamlit as st
import pandas as pd



def get_coin_prices(coin_list):
    frames = []
    for coin_name in coin_list:
        print(coin_name)
        df_price = pd.DataFrame.from_dict(cg.get_coin_market_chart_by_id(id=coin_name, vs_currency='usd', days=364))
        df = pd.DataFrame()
        df[coin_name] = [i[1] for i in df_price["prices"]]
        df.index = [datetime.fromtimestamp(int(i[0])/1000.0) for i in df_price["prices"]]
        frames.append(df)
    df = pd.concat(frames, axis=1)
    df.index.name = "Date"
    return df

df_ticker = pd.read_csv('tickers.csv')

def get_coin_name_list(symbol_list):
    l = []
    for c in symbol_list:
        c = c.lower()
        name = df_ticker[df_ticker["symbol"] == c]
    l.append(name)
    return l


# Iterates over each of the fields from Lunar Crush, gets the value from Lunar Crush and renders it with the field name
def main():

    coin_list = ["bitcoin", "ethereum", "cardano", "litecoin", "solana", "pancakeswap-token", "ripple", "polkadot", "binancecoin"]
    symbol_list = ['ADA', 'ETH', 'AGI', 'LINK', 'SOL', 'LTC', 'COTI', 'ETC' '1inch']

    print(get_coin_name_list(symbol_list))
    df = get_coin_prices(coin_list).dropna()
    #returns = df.to_returns()
   


if __name__ == '__main__':
    main()