import os
import optparse
import sqlite3

from think import Timer


def print_profile(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT FULLNAME, SKYPENAME, CITY, COUNTRY, DATETIME(PROFILE_TIMESTAMP, 'UNIXEPOCH') FROM ACCOUNTS;")
    for row in c:
        print('[*] -- Found Account --')
        print('[+] User           : %s' % str(row[0]))
        print('[+] Skype Username : %s' % str(row[1]))
        print('[+] Location       : %s, %s' % (str(row[2]), str(row[3])))
        print('[+] Profile Date   : %s' % str(row[4]))


def print_contacts(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT DISPLAYNAME, SKYPENAME, CITY, COUNTRY, PHONE_MOBILE, BIRTHDAY FROM CONTACTS;")
    for row in c:
        print('[*] -- Found Contact --')
        print('[+] User           : %s' % str(row[0]))
        print('[+] Skype Username : %s' % str(row[1]))
        if str(row[2]) != '' and str(row[2]) != 'None':
            print('[+] Location       : %s, %s' % (str(row[2]), str(row[3])))
        if str(row[4]) != 'None':
            print('[+] Mobile Number  : %s' % str(row[4]))
        if str(row[5]) != 'None':
            print('[+] Birthday       : %s' % str(row[5]))


def print_call_log(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT DATETIME(BEGIN_TIMESTAMP, 'UNIXEPCH'), IDENTITY FROM CALLS, CONVERSATIONS WHERE CALLS.CONV_DBID = CONVERSATIONS.ID;")
    print('[*] -- Found Calls --')
    for row in c:
        print('[+] Time: %s | Partner: %s' % (str(row[0]), str(row[1])))


def print_messages(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT DATETIME(TIMESTAMP, 'UNIXEPCH'), DIALOG_PARTNER, AUTHOR, BODY_XML FROM MESSAGES;")
    print('[*] -- Found Messages --')
    for row in c:
        try:
            if 'partlist' not in str(row[3]):
                if str(row[1]) != str(row[2]):
                    msg_direction = 'To %s:' % str(row[1])
            msg_direction = 'From %s:' % str(row[2])
            print('Time: %s %s %s' % (str(row[0]), msg_direction, str(row[3])))
        except Exception as e:
            pass



timer = Timer()
timer.start()




skype_db = 'main.db'

print_profile(skype_db)
print_contacts(skype_db)
print_call_log(skype_db)
print_messages(skype_db)




timer.stop()
print(timer.get_msg())
