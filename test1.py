import requests

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"

symbol = "AAPL"
base_url = "https://paper-api.alpaca.markets/v2"

# Get last trade for AAPL
last_trade_url = f"{base_url}/stocks/{symbol}/trades/last"
headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": API_SECRET}
response = requests.get(last_trade_url, headers=headers)

if response.status_code == 200:
    last_trade = response.json()
    price = last_trade["price"]
    print(f"Current price of {symbol}: {price}")
else:
    print(f"Failed to get last trade for {symbol}. Status code: {response.status_code}")
