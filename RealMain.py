import requests
import time

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
market_status = False
BASIC_URL = "https://paper-api.alpaca.markets/v2"
counter = 0
symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET,
}

response = requests.get('https://paper-api.alpaca.markets/v2/clock', headers=headers)

if response.status_code == 200: 
  clock_info = response.json()
else:
  print("Couldn't connect to the server...")

if clock_info['is_open'] == True:
  print("The Market is open!")
  market_status = True
else:
  print("The Market is closed!")


def PlaceBuyAAPL(actual_price):
  order_data = {
      "symbol": "AAPL",
      "qty": 30,
      "side": "buy",
      "type": "market",
      "time_in_force": "day",
  }

  ORDER_URL = "https://paper-api.alpaca.markets/v2/orders"

  r = requests.post(ORDER_URL, json=order_data, headers=headers)
  
  print(f"{order_data['qty']} {order_data['symbol']} stock(s) bought at {actual_price} each!")

  return actual_price

def PlaceSellAPPL(actual_price):
  order_data = {
      "symbol": "AAPL",
      "qty": 30,
      "side": "sell",
      "type": "market",
      "time_in_force": "day",
  }

  ORDER_URL = "https://paper-api.alpaca.markets/v2/orders"

  r = requests.post(ORDER_URL, json=order_data, headers=headers)

  print(order_data['qty'], order_data['symbol'], "stocks sold at", actual_price, "each!")

  return actual_price

def FindPrice():
  current = requests.get(last_trade_url, headers=headers)
  current_json = current.json()
  current_price = current_json['trade']
  actual_price = current_price['p']

  return actual_price


def WaitForRise(last_value): 
  true_var = True

  while true_var == True: #Wait for a rise to buy
    actual_price = FindPrice()

    if actual_price > (last_value * 1.0001): #(CHANGE VALUE LATER) If rise, then buy
      last_bought = PlaceBuyAAPL(actual_price)  #Prone to error !!!!!!!!
      return last_bought
      true_var = False

    else: 
      last_value = actual_price
      time.sleep(10)
      

def WaitForFall(last_value):  # Probably Wrong
  true_var = True

  while true_var == True: #Wait for a fall
    actual_price = FindPrice()

    if actual_price < (last_value * 0.9999): #(CHANGE VALUE LATER) If fall, then sell
      last_sold = PlaceSellAPPL(actual_price)
      return last_sold
      true_var = False
        
    else: 
      last_value = actual_price
      time.sleep(15)

def UptrendDetector():
  print("Waiting for an uptrend to buy...")
  
  while True:
    actual_price = FindPrice()
    first_low = WaitForRise(actual_price)

    actual_price = FindPrice()
    first_high = WaitForFall(actual_price)
    
    actual_price = FindPrice()
    new_low = WaitForRise(actual_price)

    actual_price = FindPrice()
    new_high = WaitForFall(actual_price)

    if (new_high > first_high) and (new_low > first_low):
      return True

def Strategy(counter):
  while True:
    uptrend = False

    actual_price = FindPrice()

    if counter == 0: 
      last_bought = PlaceBuyAAPL(actual_price)
      counter += 1

    print(actual_price)
    time.sleep(30)

    while (uptrend == False):


    

if market_status == True:
  Strategy(counter)
else: 
  print("Market is down, cannot buy.")
