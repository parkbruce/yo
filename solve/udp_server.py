import socket


host = '192.168.0.103'
port = 91
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((host, port))
    s.settimeout(5)
    data, addr = s.recvfrom(1024)
    print('[+] Received from', addr)
    print('[+] Obtained', data)
    s.close()
except socket.timeout as e:
    print('[-] %s' % str(e))
    s.close()
