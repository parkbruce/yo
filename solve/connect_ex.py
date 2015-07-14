import socket


rmip = '127.0.0.1'
ports = [22,23,80,912,135,445,20]

for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((rmip, p))
    print('[+] %d:%s' % (p, result))
    s.close()
