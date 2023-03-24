import alpaca_trade_api as alpaca

account_id = "8774143a-7efb-41d6-90ce-80f52bc1eed4"
api_key = "PKMRS0PD5QOPSB14455X"
api_secret_key = "RooSe7SdHmP3vQB1cshk2LxHZ5vY2lbjDu7v5cWD"
alpaca_url = "https://paper-api.alpaca.markets"

class PythonTradingBot :
  def __init__(self):
    self.alpaca = tradeapi.REST(api_key, api_secret_key, alpaca_url, api_version='v2')
  def run(self):
    #On each minute
    async def on_minute(conn, channel, bar):
      if bar.close >= bar.open and (bar.open - bar.low) > 0.1: 
        print("Buying on Doji Candle")
        self.alpaca.submit_order("MSFT", 1, "buy", "market", "day")


