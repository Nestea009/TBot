import requests
import time

API_KEY = "PKMRS0PD5QOPSB14455X"
API_SECRET = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
BASIC_URL = "https://paper-api.alpaca.markets/v2"
symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': API_SECRET
}

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

    if actual_price > (initial_value * 1.0033): #(CHANGE VALUE LATER) If rise, then buy
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

    if actual_price < (initial_value * 0.9967): #(CHANGE VALUE LATER) If fall, then sell
      return actual_price # A fall has been found
        
    else: 
      count += 1
      time.sleep(10)

    if count >= 5:
      initial_value = FindPrice()
      count = 0

def UptrendDetector():
  print("Waiting for an uptrend to buy...")
  
  while True:
    first_low = WaitForRise()
    #print("First Low = ", first_low)

    first_high = WaitForFall()
    #print("First High = ", first_high)
    
    new_low = WaitForRise()
    #print("New Low = ", new_low)

    new_high = WaitForFall()
    #print("New High = ", new_high)

    final_low = WaitForRise()
    #print("Final Low = ", final_low)

    if (new_high > first_high * 0.999) and (new_low > first_low * 0.999) and (final_low > new_low * 0.999):
      return True

def Strategy():
  while True:

    with open("txt_files/server_status.txt", "r") as f: 
        content = f.read().strip()
        server_status = content

    while server_status == "On":

      uptrend = UptrendDetector()   
      counter = 0       
      new_HH_found = False

      while uptrend == True:    #If we're on an uptrend

        actual_price = FindPrice()

        if counter == 0: 
          print("Looking for a window...")    # Look for a window
          initial_highest_high = WaitForFall()
          last_highest_high = initial_highest_high
          print("Window found!")
          lowest_low = PlaceBuyAAPL(actual_price)   # Buy at the first rise you see
          last_low = lowest_low
          counter += 1

        window = last_highest_high - lowest_low   # Define our window
        #print("The current window is of a ", window, " difference.")
        
        if actual_price < last_low * 0.99:   # If we lost  money, sell at a loss (0.99 is for the initial price)
          PlaceSellAPPL()   
          print ("Sold at the lowest low, only lost tramit fees")
          uptrend = False
        
        with open('txt_files/High.txt', 'r') as f:  
            content = f.read().strip()
            if content == 'High':         #Every time we find a High
              #print("Found a High")
              new_high = FindPrice()

            if new_high < last_highest_high:  #If we are below the last high, sell
              PlaceSellAPPL(actual_price)
              print("Sold because uptrend is over (new lower high)")
              uptrend = False
            elif new_high >= last_highest_high:
              last_highest_high = actual_price     #If we're not, tag it as the new last high

            with open("txt_files/High.txt", "w") as f:
                  content = f.write("")

        with open("txt_files/Low.txt", "r") as f: 
            content = f.read().strip()
            if content == "Low":          #Every time we find a Low
              #print("Found a Low")
              new_low = FindPrice(actual_price)
              if new_low < last_low:  #If we are below the last low, sell
                WaitForFall()
                PlaceSellAPPL()
                print("Sold because uptrend is over (new lower low)")
                uptrend = False
              elif new_low >= last_low:  #If we're not, tag it as the new last low
                last_low = new_low
              with open("txt_files/Low.txt", "w") as f:
                  content = f.write("")

        with open("txt_files/server_status.txt", "r") as f: 
            content = f.read().strip()
            server_status = content

        
        #print(actual_price)   #Print and repeat
        time.sleep(20)

Strategy()
