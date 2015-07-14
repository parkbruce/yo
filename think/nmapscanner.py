#!/usr/bin/env python
import optparse, nmap
from threading import Thread

from ip_list import rpi_ip, docker_ip, think_ip




def nmap_scan(host, port):
    nm = nmap.PortScanner()
    nm.scan(host, port)
    state = nm[host]['tcp'][int(port)]['state']
    if state == 'open':
        print('[*] %s tcp/%s %s' % (host, port, state))




for port in range(1, 65535):
    t = Thread(target=nmap_scan, args=(rpi_ip, str(port)))
    t.start()




# parser = optparse.OptionParser('usage%prog -H <target host> -p <target port>')
# parser.add_option('-H', dest='host', type='string', help='specify target host')
# parser.add_option('-p', dest='ports', type='string', help='specify target port(s) separated by commas')
# (options, args) = parser.parse_args()
# host = options.host
# ports = options.ports.split(',')
# if (host == None) | (ports[0] == None):
    # print(parser.usage)
    # exit(0)
