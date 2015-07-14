import time
import crypt
import threading
import collections

from think import Timer

# crypt produces diff answer each time
# use SHA-512 from hashlib library

#TODO lowercase and uppercase


def get_userdict(fn='shadow-'):
    userdict = dict()
    for line in open(fn):
        uname, crypt_pw, *_ = line.split(':')
        userdict[uname] = crypt_pw
    return userdict


def get_crypt_pw(uname):
    return get_userdict()[uname]


def get_salt(crypt_pw=None, uname=None):
    if crypt_pw:
        return crypt_pw[:19]
    elif uname:
        return get_crypt_pw(uname)[:19]


def guess(guess, crypt_pw):
    salt = get_salt(crypt_pw=crypt_pw)
    if crypt.crypt(guess, salt) == crypt_pw:
        print('[+] Password: %s' % guess)
        return guess


def brute_guess(crypt_pw, dict_fn):
    for line in open(dict_fn):
        word = line.strip('\n')
        t = threading.Thread(target=guess, args=(word, crypt_pw))
        t.start()




timer = Timer()
timer.start()




uname = 'matt'
crypt_pw = get_crypt_pw(uname)


print('[*] crack.py\n\n')
print('[+] Username       : %s' % uname)
print('[+] Crypt Password : %s' % crypt_pw)
print('[+] Brute Guessing...')

brute_guess(crypt_pw, dict_fn='words')




timer.stop()
print(timer.get_msg())
# 285
