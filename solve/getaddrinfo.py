import socket


def get_portnumber(prefix):
    return dict( (getattr(socket, a), a) for a in dir(socket) if a.startswith(prefix))


proto_fam = get_portnumber('AF_')
types = get_portnumber('SOCK_')
protocols = get_portnumber('IPPROTO_')

def print_socket_info(family, s_type, proto, canonname, s_addr):
    print('[+] ===============')
    print('[+] Family         :', proto_fam[family])
    print('[+] Type           :', types[s_type])
    print('[+] Protocol       :', protocols[proto])
    print('[+] Canonical name :', canonname)
    print('[+] Socket address :', sockaddr)


site_name = 'www.google.com'

print('[+] %s' % site_name)

for info in socket.getaddrinfo(site_name, 'http'):
    family, s_type, proto, canonname, s_addr = info
    print_socket_info(family, s_type, proto, canonname, s_addr)
