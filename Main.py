import os
from multiprocessing import Process

def script1():
  os.system("python ./RealMain.py")

def script2():
  os.system("python ./H.py")

def script3():
  os.system("python ./L.py")

def script4():
  os.system("python ./Server_status.py")

if __name__ == '__main__':
  p = Process(target=script1)
  q = Process(target=script2)
  s = Process(target=script3)
  t = Process(target=script4)
  p.start()
  q.start()
  s.start()
  t.start()
  p.join()
  q.join()
  s.join()
  t.join()
