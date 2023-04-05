#First Strategy

if actual_price > (last_bought * 1.001):
  PlaceSellAPPL()
  print("Sold because benefit!")
  time.sleep(120)
  last_bought == PlaceBuyAAPL()

if actual_price < (last_bought * 0.999):
  PlaceSellAPPL()
  print("Sold because loss...")
  print(last_bought, actual_price)
  time.sleep(300)
  last_bought == PlaceBuyAAPL()

#Stuff to do 

#1. Organize the "actual_price" things into a def to not repeat that much code
#2. Finish current rules
#3. Make a def for "WAIT FOR A RISE" and "WAIT FOR A FALL"
#4. Do more rules
#5. Organize everything



