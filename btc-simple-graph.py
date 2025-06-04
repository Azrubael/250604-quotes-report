import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

exchange = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1d'
prolongation = 365
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

# Обчислення середньої ціни за день
data['average_price'] = (data['high'] + data['low']) / 2

# Обчислення 50-денного ковзного середнього
data['MA50'] = data['average_price'].rolling(window=50).mean()

# Будування простого графіка котировок
plt.figure(figsize=(18, 6))
plt.plot(data.index, data['average_price'], label='Avg price BTC/USDT', color='blue')
plt.plot(data.index, data['MA50'], label='MA50', color='red')
plt.title('The graph of quotes BTC/USDT for 365 days')
plt.xlabel('Date')
plt.ylabel('USDT price')
plt.legend()
plt.grid()

# Здереження графік у файл
graph_file = 'btc_price_graph.png'
plt.savefig(graph_file)
plt.close()
print(f'Графік котировок {symbol} за останні {prolongation} збережено в файл {graph_file}')
