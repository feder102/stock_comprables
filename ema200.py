import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from ta.trend import EMAIndicator
# Lista de acciones
stocks = [
    "BABA", "AAPL", "ADBE", "AMD", "AMGN", "AMX", "AMZN",
    "BB", "BHP", "BIDU", "BIIB", "BITF", "BP", "CS", "CSCO",
    "CVX", "EBAY", "ERIC", "META", "GLOB", "GOLD", "GOOGL", "HMY",
    "HSBC", "HUT", "IBM", "IBN", "INFY", "INTC", "JD", "MELI", "MFG", "MSFT", "MSI", 
    "MSTR", "MUFG","NFLX", "NG", "NVDA", "PBR", "PSX", "V"
]
stocks_comprables = []

def fun_ema(stock):
    # Fecha de inicio (hace 3 meses)
    start_date = datetime.now() - timedelta(days=201)
    stock = stock[-1]
    # Descargar datos históricos
    # data = yf.download(stock, interval="1d",start=start_date)
    data = yf.download(stock, interval="1d",period='1y')

    # Crear un nuevo DataFrame para almacenar las EMA200
    ema200 = pd.DataFrame()
    ema = EMAIndicator(close=data["Close"], window=200)
    ema200 = ema.ema_indicator()
    ema200 = ema200.iloc[-1]
    price = data['Close'].iloc[-1]
    distance = abs((ema200 - price) / ema200) * 100

    if ema200 < price and distance <= 5:
        stocks_comprables.append(stock)
    # else:
    #     print(f"{stock}: La EMA200 está por debajo del precio y a una distancia del 5%")

if __name__ == '__main__':
    split_stocks = list(map(lambda stock: stock.split(','), stocks))
    list(map(fun_ema, split_stocks))
    print(stocks_comprables)

