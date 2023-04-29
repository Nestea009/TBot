import time
time.sleep(30)

print("Found a High!")

with open('High.txt', 'w') as f:
        f.write('High')