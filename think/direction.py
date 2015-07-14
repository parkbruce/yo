import dpkt, socket


def print_pcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: %s --> Dst: %s' % (src, dst))
        except Exception as e:
            pass


# with open('geotest.pcap') as f:
f = open('geotest.pcap')
pcap = dpkt.pcap.Reader(f)
print_pcap(pcap)
