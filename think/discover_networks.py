# from winreg import OpenKey, EnumKey, EnumValue, CloseKey
import os
import optparse
import mechanize
import urllib
import re
import urlparse


# def print_nets():
    # net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    # key = OpenKey(HKEY_LOCAL_MACHINE, net)
    # print('[*] Networks you have joined.')
    # for i in range(100):
        # try:
            # guid = EnumKey(key, i)
            # net_key = OpenKey(key, str(guid))
            # (n, addr, t) = EnumValue(net_key, 5)
            # (n, name, t) = EnumValue(net_key, 4)
            # mac_addr = val2addr(addr)
            # net_name = str(name)
            # print('[+] %s %s' % (net_name, mac_addr))
            # CloseKey(net_key)
        # except Exception as e:
            # break


def val2addr(val):
    addr = ''
    for ch in val:
        addr += ('%02x ' % ord(ch))
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr


def wigle_print(username, pw, netid):
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    req_data = urllib.urlencode({'credential_0': username, 'credential_1': pw})
    browser.open('https://wigle.net/gps/gps/main/login', req_data)
    params = {}
    params['netid'] = netid
    req_params = urllib.urlencode(params)
    res_url = 'http://wigle.net/gps/gps/main/confirmquery/'
    res = browser.open(res_url, req_params).read()
    map_latitude = 'N/A'
    map_longitude = 'N/A'
    rlatitude = re.findall(r'maplat=.*\&', res)
    if rlatitude:
        map_latitude = rlatitude[0].split('&')[0].split('=')[1]
    rlongitude = re.findall(r'maplon=.*\&', res)
    if rlongitude:
        map_longitude = rlongitude[0].split
    print('[-] Latitude: %s, Longitude: %s' % (map_latitude, map_longitude))
