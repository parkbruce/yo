#!/usr/bin/env python
import sys, optparse, socket
from threading import Thread, Semaphore

from ip_list import rpi_ip, docker_ip, think_ip


# socket errors:
# herror - address-related error
# timeout - timeout on a socket
# gaierror - raised from getaddrinfo() and getnameinfo()
# error - socket-related errors



def get_vulnerabilities(banner, fn='vulnerabilities.txt'):
    for line in open(fn, 'r'):
        #TODO this will cause error
        banner, vulnerability = line.strip('\n').split(':')
        if banner == banner_vuln[0]:
            return banner_vuln[1].split(', ')


# screen_lock = Semaphore(value=1)
def scan_socket(host, port):
    try:
        # socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #TODO try createconnection
        s.connect((host, port))

        # s.send('ViolentPython\r\n')
        # maybe it is 100 for hostname and 1024 for ip
        # banner = s.recv(100)
        banner = s.recv(1024)

        screen_lock.acquire()
        print('[+] %s/%d: %s' % (host, port, banner))
        s.close()

    #TODO use socket.timeout
    except socket.timeout as st:
        print('[-] Error: %s' % str(e))
        s.close()
    except Exception as e:
        # screen_lock.acquire()
        # print('[-] Error: %s' % str(e))
        # print('[-] %d/tcp closed' % port)
        s.close()

    # finally:
        # screen_lock.release()
        # s.close()


def scan_ports(host, ports):
    try:
        host_ip = socket.gethostbyname(host)
    except Exception as e:
        try:
            hostname = socket.gethostbyaddr(host)
            # print('[+] Scan Results for: %s' % hostname[0])
        except Exception as e:
            # print('[-] Error: %s' % str(e))
            # print('[+] Scan Results for: %s' % host_ip)
            return

    for port in ports:
        t = Thread(target=scan_socket, args=(host, port))
        t.start()


def scan_all_ports(host):
    all_ports = [port for port in range(1, 65535)]
    scan_ports(host, all_ports)


def scan_hosts(hosts):
    for host in hosts:
        t = Thread(target=scan_all_ports, args=(host))
        t.start()


def scan_all_hosts(ip_prefix):
    scan_hosts(['%s.%d' % (ip_prefix, host) for host in range(1,255)])


def scan_all_subnets(ip_prefix, host=None):
    if host:
        for subnet in range(1, 255):
            hosts = ['%s.%d.%d' % (ip_prefix, subnet, host) for subnet in range(1,255)]
            t = Thread(target=scan_hosts, args=(hosts))
            t.start()
    else:
        for subnet in range(1, 255):
            ip_subnet = '%s.%d' % (ip_prefix, subnet)
            t = Thread(target=scan_all_hosts, args=(ip_subnet))
            t.start()


scan_all_ports(rpi_ip)



# parser = optparse.OptionParser('%s -H <host> -p <port>' % sys.argv[0])
# parser.add_option('-H', dest='target_host', type='string', help='specify target host')
# parser.add_option('-p', dest='target_ports', type='string', help='specify target port(s) separated by comma')
# (options, args) = parser.parse_args()
# host = options.target_host
# ports = options.target_ports.split(',')
# if (host == None) | (ports == None):
    # print(parser.usage)
    # exit(0)
