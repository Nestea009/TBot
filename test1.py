import time

# variable to be changed by test2.py
x = False

while True:
    # check if x has been changed by test2.py
    with open('shared_file.txt', 'r') as f:
        content = f.read().strip()
        if content == 'True':
            x = True
        else:
            x = False

    print(f'x = {x}')
    time.sleep(1)