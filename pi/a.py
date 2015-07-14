import ftplib

session = ftplib.FTP('server.IP.address.com', 'USERNAME', 'PASSWOrD')
file = open('*.cap', 'rb')
session.storbinary('STOR *.cap', file)
file.close()
session.quit()
