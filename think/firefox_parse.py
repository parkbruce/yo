import os
import optparse
import sqlite3
import re


def print_downloads(download_db):
    conn = sqlite3.connect(download_db)
    c = conn.cursor()
    c.execute("SELECT NAME, SOURCE, DATETIME(ENDTIME/1000000, 'UNIXEPOCH' FROM MOZ_DOWNLOADS;")
    print('[*] --- Files Downloaded ---')
    for row in c:
        print('[+] File: %s from source: %s at: %s' % (str(row[0]), str(row[1]), str(row[2])))

def print_cookies(cookies_db):
    try:
        conn = sqlite3.connect(cookies_db)
        c = conn.cursor()
        c.execute("SELECT HOST, NAME, VALUE FROM MOZ_COOKIES")
        print('[+] -- Found Cookies --')
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            print('[+] Host: %s, Cookie: %s, Value: %s' % (host, name, value))
    except Exception as e:
        if 'encrypted' in str(e):
            print('[-] Error reading your cookies database.')
            print('[-] Upgrade your Python-Sqlite3 Library')


def print_history(places_db):
    try:
        conn = sqlite3.connect(places_db)
        c = conn.cursor()
        c.execute("SELECT URL, DATETIME(VISIT_DATE/1000000, 'UNIXEPOCH') FROM MOZ_PLACES, MOZ_HISTORYVISITS WHERE VISIT_COUNT > 0 AND MOZ_PLACES.ID==MOZ_HISTORYVISITS.PLACE_ID;")
        print('[+] -- Found History --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
            print('[+] %s - Visited: %s' % (date, url))
    except Exception as e:
        if 'encrypted' in str(e):
            print('[-] Error reading the places database.')
            print('[-] Upgrade your Python-Sqlite3 Library')
            exit(0)


def print_google(places_db):
    conn = sqlite3.connect(places_db)
    c = conn.cursor()
    c.execute("SELECT URL, DATETIME(VISIT_DATE/1000000, 'UNIXEPOCH') FROM MOZ_PLACES, MOZ_HISTORYVISITS WHERE VISIT_COUNT > 0 AND MOZ_PLACES.ID==MOZ_HISTORYVISITS.PLACE_ID;")
    print('[+] -- Found Google --')
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)
            if r:
                search=r[0].split('&')[0]
                search=search.replace('q=', '').replace('+', ' ')
                print('[+] %s - Searched For: %s' % (date, search))



firefox_path = '/home/matt/.mozilla/firefox/vyiaax6v.default/'
cookies_db = os.path.join(firefox_path, 'cookies.sqlite')
places_db = os.path.join(firefox_path, 'places.sqlite')


print_cookies(cookies_db)
# print_google(places_db)
# print_history(places_db)
