import socket


host = '192.168.0.103'
port = 91
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s.sendto(b'hello all', (host, port)))
s.close()
