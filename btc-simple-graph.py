import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

exchange = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1d'
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, start_date, end_date)