import time

while True:
    # change the value of x in shared_file.txt
    with open('shared_file.txt', 'w') as f:
        f.write('True')

    time.sleep(10)

    with open('shared_file.txt', 'w') as f:
        f.write('False')

    time.sleep(10)