import yfinance as yf
import pandas as pd
import ta

def fetch_stock_data(ticker, period="3mo", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    if data.empty:
        raise ValueError("Invalid ticker or no data available.")
    return data

def analyze_stock(ticker):
    df = fetch_stock_data(ticker)

    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)

    latest = df.iloc[-1]

    if latest['Close'] > latest['SMA_20'] and latest['RSI'] < 70:
        return "BUY"
    elif latest['RSI'] > 80:
        return "SELL"
    else:
        return "HOLD"
