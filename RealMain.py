import requests
import time

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
market_status = False
BASIC_URL = "https://paper-api.alpaca.markets/v2"
symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET
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


def WaitForRise():      #ALL OF THIS IS FLOOD
  true_var = True
  count = 0
  initial_value = FindPrice()

  while true_var == True: #Wait for a rise to buy
    actual_price = FindPrice()

    if actual_price > (initial_value * 1.0001): #(CHANGE VALUE LATER) If rise, then buy
      return actual_price # A rise has been found

    else: 
      count += 1
      time.sleep(10)

    if count >= 5:
      initial_value = FindPrice()
      count = 0
      

def WaitForFall():         #ALL OF THIS IS FLOOD
  true_var = True
  count = 0
  initial_value = FindPrice()

  while true_var == True: 
    actual_price = FindPrice()

    if actual_price < (initial_value * 0.9999): #(CHANGE VALUE LATER) If fall, then sell
      return actual_price # A fall has been found
        
    else: 
      count += 1
      time.sleep(10)

    if count >= 5:
      initial_value = FindPrice()
      count = 0

def FindHighestHigh():
  initial_highest_high = WaitForFall()
  return initial_highest_high


def UptrendDetector():
  print("Waiting for an uptrend to buy...")
  
  while True:
    first_low = WaitForRise()
    print("First Low = ", first_low)

    first_high = WaitForFall()
    print("First High = ", first_high)
    
    new_low = WaitForRise()
    print("New Low = ", new_low)

    new_high = WaitForFall()
    print("New High = ", new_high)

    if (new_high > first_high) and (new_low > first_low):
      return True

def FindLow(): 
  return "ERR" #For this to work we need 2 highs
  

def Strategy():
  while True:
    uptrend = UptrendDetector()   
    counter = 0       
    new_HH_found = False

    while uptrend == True:    #If we're on an uptrend

      actual_price = FindPrice()

      if counter == 0: 
        print("Looking for a window...")    # Look for a window
        initial_highest_high = FindHighestHigh()
        last_highest_high = initial_highest_high
        print("Window found!")
        WaitForRise()
        lowest_low = PlaceBuyAAPL(actual_price)   # Buy at the first rise you see
        last_low = lowest_low
        counter += 1

      window = last_highest_high - lowest_low   # Define our window
      print("The current window is of a ", window, " difference.")
       
      if actual_price < lowest_low * 0.99:   # If we lost  money, sell at a loss (0.99 is for the initial price)
        PlaceSellAPPL()   # Revise all of this, because Risk == Gainz
        print ("Sold at the lowest low, only lost tramit fees")
        uptrend = False

      if (actual_price > last_highest_high) and (actual_price < (initial_highest_high * 1.25)):
         last_highest_high = actual_price     # If you find a higher high, set it as such
      
      #Execute the following if we detect a new high:
      #--------------------------------------------------------------------------------------------------------
      new_low = FindLow() # Make the function look for a low for like 10s, if it doestn't find, return 0

      if new_low != 0:
        if new_low < last_low: 
          WaitForFall()
          PlaceSellAPPL()
          print("Sold because uptrend is over")
          uptrend = False
        elif new_low > last_low:
          last_low = new_low
      #--------------------------------------------------------------------------------------------------------

      print(actual_price)   #Print and repeat
      time.sleep(20)

def Test():       # ERASE LATER
  while True:
    print(FindPrice())
    with open('High.txt', 'r') as f:
        content = f.read().strip()
        if content == 'High':
            print("Sell!!")
            with open("High.txt", "w") as f:
                content = f.write("")

    with open("Low.txt", "r") as f:
      content = f.read().strip()
      if content == "Low":
        print("Buy!!")
        with open("Low.txt", "w") as f:
            content = f.write("")

    time.sleep(3)


if market_status == True:
  #Strategy()
  Test()
else: 
  Test()
  print("Market is down, cannot buy.")
