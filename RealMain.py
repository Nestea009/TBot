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

  last_trade_url = f"https://data.alpaca.markets/v2/stocks/{order_data['symbol']}/trades/latest"
  price = requests.get(last_trade_url, headers=headers)
  last_json_bought = price.json()
  last_trade_bought = last_json_bought['trade']
  last_bought = last_trade_bought['p']

  r = requests.post(ORDER_URL, json=order_data, headers=headers)
  
  print(f"{order_data['qty']} {order_data['symbol']} stock(s) bought at {last_bought} each!")

  return last_bought

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

  print(order_data['qty'], order_data['symbol'], "stocks sold at", actual_price, "each!")

  return r.content


def WaitForRise(last_value): 
  true_var = True

  while true_var == True: #Wait for a rise to buy
    current = requests.get(last_trade_url, headers=headers)
    current_json = current.json()
    current_price = current_json['trade']
    actual_price = current_price['p']

    if actual_price > (last_value * 1.001): #(CHANGE VALUE LATER) If rise, then buy
      last_bought = PlaceBuyAAPL()  #Prone to error !!!!!!!!
      true_var = False

    else: 
      last_value = actual_price
      time.sleep(10)
      

def WaitForFall(last_value):
  true_var = True

  while true_var == True: #Wait for a fall
    current = requests.get(last_trade_url, headers=headers)
    current_json = current.json()
    current_price = current_json['trade']
    actual_price = current_price['p']

    if actual_price < (last_value * 0.9999): #(CHANGE VALUE LATER) If fall, then sell
      PlaceSellAPPL()
      true_var = False
        
    else: 
      last_value = actual_price
      time.sleep(15)


def Strategy(counter):
  while True:
    current = requests.get(last_trade_url, headers=headers)
    current_json = current.json()
    current_price = current_json['trade']
    actual_price = current_price['p']

    if counter == 0: 
      last_bought = PlaceBuyAAPL()
      counter += 1

    print(actual_price)
    time.sleep(30)

    #Rule 1
    #If we're winning money, wait for a maximmum and sell
    #Then wait for a rise and buy

    if actual_price > (last_bought * 1.001): #If we're winning money

      WaitForFall(actual_price)
      WaitForRise(actual_price)
            
    #Rule 2
    #If we're loosing money, do not wait, sell inmediately
    #Wait for a minnimum to buy, but if fall continues sell inmediately

    if actual_price < (last_bought * 0.999): #If we're loosing money
      true_var = True
      last_lost = actual_price
      time.sleep(5) #Wait for the price to change
      current = requests.get(last_trade_url, headers=headers)
      current_json = current.json()
      current_price = current_json['trade']
      actual_price = current_price['p']

      if actual_price < last_lost: # If we're still loosing
        PlaceSellAPPL() # Sell at a loss
        WaitForRise(actual_price) 

      elif actual_price >= last_lost: #However, if we're suddenly winning
        WaitForFall(actual_price)
        WaitForRise(actual_price) 


    #Rule 3
    #If market is going to close, sell (?)
    

if market_status == True:
  Strategy(counter)
else: 
  print("Market is down, cannot buy.")


