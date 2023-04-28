import os
from multiprocessing import Process

def script1():
    os.system("test1.py")     
def script2():
    os.system("test2.py") 

if __name__ == '__main__':
    p = Process(target=script1)
    q = Process(target=script2)
    p.start()
    q.start()
    p.join()
    q.join()