import socket











host = '192.168.0.103'
port = 1991
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
conn, addr = s.accept()
print('[+] Client: %s' % str(addr))
msg = bytes('[+] Server: %s' % str(conn.getsockname()), 'utf-8')
conn.send(msg)
conn.close()
