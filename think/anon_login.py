import ftplib


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('[*] %s FTP Anonymous Logon Succeeded.' % str(hostname))
        ftp.quit()
        return True
    except Exception as e:
        print('[-] %s' % e)
        return False


host = '192.168.0.117'
anon_login(host)
