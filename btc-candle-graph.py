import ccxt
import pandas as pd
import mplfinance as mpf
from datetime import datetime, timedelta

exchange = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1w'
prolongation = 365 * 3
end_date = datetime.now()
start_date = end_date - timedelta(days=prolongation)

# Конвертація даних в мілісекунди
start_timestamp = int(start_date.timestamp() * 1000)
end_timestamp = int(end_date.timestamp() * 1000)

# Зчитування історичних даних для symbol
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=start_timestamp, limit=prolongation)

# Перетворення даних в DataFrame
data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data.set_index('timestamp', inplace=True)

# Обчислення 50-денного ковзного середнього
data['average_price'] = (data['high'] + data['low']) / 2
data['MA50'] = data['average_price'].rolling(window=50).mean()

# Налаштування стилю для свічок
mc = mpf.make_marketcolors(up='green', down='red', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)

# Здереження графіка у файл
graph_file = 'pics/btc_candle_graph.png'
mpf.plot(data, type='candle', style=s, title='The graph of quotes BTC/USDT for 365 days',
         ylabel='USDT price', volume=False, addplot=mpf.make_addplot(data['MA50'], color='blue'), savefig=graph_file)

print(f'Графік котировок {symbol} за останні {prolongation} збережено в файл {graph_file}')
