import time
import threading
import optparse
import zipfile

import think
from think import Timer


def guess(zf, pw):
    try:
        zf.extractall(pwd=bytes(pw, 'utf-8'))
        print('[+] Password: %s' % pw)
    except Exception as e:
        pass


def brute_guess(zf, dict_fn):
    for line in open(dict_fn):
        word = line.strip('\n')
        t = threading.Thread(target=guess, args=(zf, word))
        t.start()


def unzip(fn):
    zf = zipfile.ZipFile(fn)
    for df in think.get_dicts():
        t = threading.Thread(target=brute_guess, args=(zf, df))
        t.start()




timer = Timer()
timer.start()




print('[*] unzip.py\n\n')

unzip('yo.zip')




timer.stop()
print(timer.get_msg())
