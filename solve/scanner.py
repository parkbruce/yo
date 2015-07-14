import time
import sys
import subprocess
import collections
import socket
import threading
from datetime import datetime


dic = collections.OrderedDict()
start_time = datetime.now()


class Scanner(threading.Thread):
    def __init__(self, prefix):
        threading.Thread.__init__(self)
        self.prefix = prefix

    def run(self):
        run1(self.prefix)


def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr,135))
    if not result:
        s.close()
        return 1
    s.close()


def run1(prefix):
    for i in range(256):
        addr = '%s.%s' % (prefix, str(i))
        if scan(addr):
            dic[ip] = addr


prefix = '192.168.0'

t = Scanner(prefix)
t.start()

# run1(prefix)

total_time = datetime.now() - start_time
print('[+] Total time: %s' % total_time)
