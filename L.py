import time
import requests

symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
  'APCA-API-KEY-ID': "PK42I07MH09F0ORJLLC1",
  'APCA-API-SECRET-KEY': "3UQQh5eNtNRdlcUgespElmCD3JqW2iDOd6AiruZd"
}

def FindPrice():
  current = requests.get(last_trade_url, headers=headers)
  current_json = current.json()
  current_price = current_json['trade']
  actual_price = current_price['p']

  return actual_price

while True: 
  count = 0
  initial_value = FindPrice()

  while True: #Wait for a rise to buy
    actual_price = FindPrice()

    if actual_price > (initial_value * 1.0033): #(CHANGE VALUE LATER) If rise, then buy
      count = 0
      initial_value = actual_price # A rise has been found
      break

    else: 
      count += 1
      time.sleep(10)

    if count >= 5:
      initial_value = FindPrice()
      count = 0
      
  with open('txt_files/Low.txt', 'w') as f:
        f.write('Low')
  time.sleep(21)