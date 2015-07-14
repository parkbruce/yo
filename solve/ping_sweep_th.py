import os
import sys
import subprocess
import socket
import collections
import platform
import threading

from datetime import datetime


net = input("Network Address ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(input("Starting Number "))
en1 = int(input("Last Number "))
en1 += 1
dic = collections.OrderedDict()

curr_os = platform.system()
if curr_os == 'Windows':
    cmd = 'ping -n 1 '
elif curr_os == 'Linux':
    cmd = 'ping -b '
else:
    cmd = 'ping -b '

t1 = datetime.now()
class myThread(threading.Thread):
    def __init__(self, st, en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        sweep(self.st, self.en)


def sweep(st1, en1):
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        ping_cmd = cmd + addr
        res = os.popen(ping_cmd)
        for line in res.readlines():
            # if line.count("TTL"):
                # break
            if line.count("TTL"):
                dic[i] = addr




total_ip = en1 - st1
tn = 2  # number of ip handled by one thread
total_thread = total_ip/tn
total_thread = int(total_thread) + 1
threads = []
try:
    for i in range(total_thread):
        en = st1 + tn
        if en > en1:
            en = en1
        t = myThread(st1, en)
        t.start()
        threads.append(t)
        st1 = en
except Exception as e:
    print(e)

print('\tNumber of Active Threads:', threading.activeCount())

for t in threads:
    t.join()
print('Exiting Main Thread')
_dict = collections.OrderedDict(sorted(dic.items()))
for k in _dict:
    print('%s --> Live' % _dict[k])

t2 = datetime.now()
total = t2-t1
print('Timer: %s' % total)
