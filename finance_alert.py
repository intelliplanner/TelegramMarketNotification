import yfinance as yf
import requests
import os

# Read secrets from environment variables
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def get_market_data():
    tickers = ["AAPL", "MSFT", "BTC-USD", "^NSEI", "^BSESN"]  # Apple, Microsoft, Bitcoin, Nifty 50, Sensex
    data = {}
    for t in tickers:
        stock = yf.Ticker(t)
        price = stock.history(period="1d")["Close"].iloc[-1]
        data[t] = round(price, 2)
    return data

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    market_data = get_market_data()
    msg = "📊 Finance Update:\n"
    for symbol, price in market_data.items():
        msg += f"{symbol}: {price}\n"
    send_to_telegram(msg)
