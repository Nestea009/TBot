import time
import requests

symbol = "AAPL"
last_trade_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades/latest"

headers = {
    'APCA-API-KEY-ID': "PKMRS0PD5QOPSB14455X",
    'APCA-API-SECRET-KEY': "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
}

while True: 
  response = requests.get('https://paper-api.alpaca.markets/v2/clock', headers=headers)

  if response.status_code == 200: 
    clock_info = response.json()
  else:
    print("Couldn't connect to the server...")

  if clock_info['is_open'] == True:
    
    with open("txt_files/server_status.txt", "r") as g:
      content = g.read().strip()
      if content != "On":
        with open('txt_files/server_status.txt', 'w') as f:
            f.write('On')
            print("The Market is now On!")
  else:
    with open("txt_files/server_status.txt", "r") as g:
      content = g.read().strip()
      if content != "Off":
        with open('txt_files/server_status.txt', 'w') as f:
            f.write('Off')
            print("The Market is now Off!")
            
  
  time.sleep(5)
