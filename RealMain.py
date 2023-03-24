import requests
import time

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"

headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET,
    'Content-Type': 'application/json'
}

def PlaceBuyAAPL():
  order_data = {
      "symbol": "AAPL",
      "qty": 1,
      "side": "buy",
      "type": "market",
      "time_in_force": "day",
  }

  ORDER_URL = "https://paper-api.alpaca.markets/v2/orders"

  r = requests.post(ORDER_URL, json=order_data, headers=headers)

  print("Stocks bought!")

  return r.content

def PlaceSellAPPL():
  order_data = {
      "symbol": "AAPL",
      "qty": 1,
      "side": "sell",
      "type": "market",
      "time_in_force": "day",
  }

  ORDER_URL = "https://paper-api.alpaca.markets/v2/orders"

  r = requests.post(ORDER_URL, json=order_data, headers=headers)

  print("Stocks sold!")

  return r.content

while API_KEY == "PKMRS0PD5QOPSB14455X":
  PlaceBuyAAPL()
  time.sleep(60)
  PlaceSellAPPL()
  time.sleep(60)

