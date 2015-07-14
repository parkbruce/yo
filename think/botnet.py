import optparse, pxssh


class Client:

    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.session = self.conn()

    def conn(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.passwd)
            return s
        except Exception as e:
            print('[-] Error: %s' % e)

    def send_cmd(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnet_cmd(cmd):
    for client in botnet:
        output = client.send_cmd(cmd)
        print('[*] Output from %s' % client.host)
        print('[+] %s' % output)

def add_client(host, user, passwd):
    client = Client(host, user, passwd)
    botnet.append(client)

botnet = []
add_client('10.10.10.110', 'root', 'toor')
add_client('10.10.10.120', 'root', 'toor')
add_client('10.10.10.130', 'root', 'toor')

botnet_cmd('uname -v')
botnet_cmd('cat /etc/issue')
