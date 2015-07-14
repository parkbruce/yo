import pygeoip


gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def print_record(target):
    rec = gi.record_by_name(target)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    print('[*] Target: %s Geo-located.' % target)
    print('[+] %s, %s, %s' % (str(city), str(region), str(country)))
    print('[+] Latitude: %s, Longitude: %s' % (str(latitude), str(longitude)))

target = '173.255.226.98'
print_record(target)
