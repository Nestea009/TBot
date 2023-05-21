import time
import requests

symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
    'APCA-API-KEY-ID': "PKMRS0PD5QOPSB14455X",
    'APCA-API-SECRET-KEY': "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
}

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

while True: 
  true_var = True
  count = 0
  initial_value = FindPrice()

  while true_var == True: #Wait for a rise to buy
    actual_price = FindPrice()

    if actual_price > (initial_value * 1.0001): #(CHANGE VALUE LATER) If rise, then buy
      count = 0
      initial_value = actual_price # A rise has been found
      true_var = False

    else: 
      count += 1
      time.sleep(10)

    if count >= 5:
      initial_value = FindPrice()
      count = 0
      
  with open('txt_files/Low.txt', 'w') as f:
        f.write('Low')
  time.sleep(5)