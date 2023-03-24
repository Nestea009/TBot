import requests
import json

# replace with your own API key and secret
APCA_API_KEY_ID = 'PKMRS0PD5QOPSB14455X'
APCA_API_SECRET_KEY = 'RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD'

# set up the API endpoint URL
endpoint = "https://paper-api.alpaca.markets/v2/orders"

# set up the request headers
headers = {
    'APCA-API-KEY-ID': APCA_API_KEY_ID,
    'APCA-API-SECRET-KEY': APCA_API_SECRET_KEY,
    'Content-Type': 'application/json'
}

# set up the order payload
order = {
    "symbol": "AAPL",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "gtc"
}

# send the request to place the order
response = requests.post(endpoint, headers=headers, json=order)

# print the response
print(response.json())