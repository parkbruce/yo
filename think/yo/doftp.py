import sys, os, socket, thread


def get_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        # print('[-] Error: %s' % str(e))
        return


def check_vulns(banner, fn):
    f = open(fn, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
        print('[+] Server is vulnerable: %s' % banner.strip('\n'))


if len(sys.argv) == 2:
    fn = sys.argv[1]
    if not os.path.isfile(fn):
        print('[-] %s does not exist' % fn)
        exit(0)
    if not os.access(fn, os.R_OK):
        print('[-] %s access denied' % fn)
        exit(0)
else:
    print('[-] Usage: %s <vuln filename>' % str(sys.argv[0]))
    exit(0)


# rpi_ip = '192.168.0.117'
# docker = '172.17.42.1'
# think = '192.168.0.115'

port_list = [p for p in range(1, 65535)]

for i in range(1, 255):
    for j in range(1, 255):
        # ip_list.append('192.168.%s.%s' % (str(i), str(j)))
        ip = '192.168.%s.%s' % (str(i), str(j))
        for port in port_list:
            banner = get_banner(ip, port)
            if banner:
                print('[+] %s  port=%d  banner=%s' % (ip, port, banner))
                check_vulns(banner, fn)
