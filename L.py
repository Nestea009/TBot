import time

time.sleep(10)
print("Found a Low!")

with open('Low.txt', 'w') as f:
        f.write('Low')