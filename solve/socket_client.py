import socket


host = '192.168.0.103'
port = 1991
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(s.recv(1024))
s.send(b'hi')

# buf = bytearray(b'')
# print('[+] %d bytes received' % s.recv_into(buf))
# print('[+] %s' % buf)

s.close()
