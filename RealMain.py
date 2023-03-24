import requests
import time

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
market_status = False
BASIC_URL = "https://paper-api.alpaca.markets/v2"
counter = 0

current = 0

headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET,
}

response = requests.get('https://paper-api.alpaca.markets/v2/clock', headers=headers)

#print(response.status_code)

if response.status_code == 200: 
  clock_info = response.json()
else:
  print("Couldn't connect to the server...")

if clock_info['is_open'] == True:
  print("The Market is open!")
  market_status = True
else:
  print("The Market is closed!")
  market_status = False


def PlaceBuyAAPL():
  order_data = {
      "symbol": "AAPL",
      "qty": 1,
      "side": "buy",
      "type": "market",
      "time_in_force": "day",
  }

  ORDER_URL = "https://paper-api.alpaca.markets/v2/orders"

    #THIS CODE BASICALLY GETS THE LAST TRADED STOCK'S PRICE
  last_trade_url = f"https://data.alpaca.markets/v2/stocks/{order_data['symbol']}/trades/latest"
  price = requests.get(last_trade_url, headers=headers)
  last_json_bought = price.json()
  last_trade_bought = last_json_bought['trade']
  last_bought = last_trade_bought['p']
  print(last_bought)


  r = requests.post(ORDER_URL, json=order_data, headers=headers)
  
  print(f"{order_data['qty']} {order_data['symbol']} stock(s) bought at {last_bought} each!")

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

if market_status == True:
  while API_KEY == "PKMRS0PD5QOPSB14455X":
    if counter == 0: 
      PlaceBuyAAPL()
      counter += 1
    #if last_bought > ()
    
else: 
  print("Market is down, cannot buy.")

