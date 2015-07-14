import sys
import time
import subprocess
import socket
import threading
import collections
from datetime import datetime

net = input("Network Address ")
st1 = int(input("Starting Number "))
en1 = int(input("Last Number "))
en1 += 1
dic = collections.OrderedDict()
net1 = net.split('.')
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a
t1 = datetime.now()

class myThread(threading.Thread):
    def __init__(self, st, en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st, self.en)

def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr,135))
    if result == 0:
        s.close()
        return 1
    else:
        s.close()

def run1(st1, en1):
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if scan(addr):
            dic[ip] = addr

total_ip = en1 - st1
tn = 20
total_thread = total_ip/tn
total_thread += 1
threads = []
try:
    for i in range(total_thread):
        print("i is ", i)
        en = st1 + tn
        if en > en1:
            en = en1
        t = myThread(st1, en)
        t.start()
        threads.append(t)
        st1 = en
except:
    print("Error: unable to start thread")

print("\t Number of Active Threads:", threading.activeCount())
for t in threads:
    t.join()
print("Exiting Main Thread")
_dict = collections.OrderedDict(sorted(dic.items()))
for k in _dict:
    print(_dict[k], "--> Live")
t2 = datetime.now()
total = t2 - t1
print("scanning complete in", total)
