import os, optparse, sqlite3


def print_tables(iphone_db):
    try:
        conn = sqlite3.connect(iphone_db)
        c = conn.cursor()
        c.execute("SELECT tbl_name FROM sqlite_master WHERE type=='table';")
        print('[*] Database: %s' % iphone_db)
        for row in c:
            print('[-] Table: %s' % str(row))
    except Exception as e:
        pass
    conn.close()


def is_message_table(iphone_db):
    try:
        conn = sqlite3.connect(iphone_db)
        c = conn.cursor()
        c.execute("SELECT tbl_name FROM sqlite_master WHERE type=='table';")
        for row in c:
            if 'message' in str(row):
                return True
    except Exception as e:
        pass


def print_message(msg_db):
    try:
        conn = sqlite3.connect(msg_db)
        c = conn.cursor()
        c.execute("SELECT datetime(date,'unixepoch'), address, text FROM message WHERE address>0;")
        for row in c:
            date = str(row[0])
            addr = str(row[0])
            text = row[2]
            print('[+] Date: %s, Addr: %s, Message: %s' % (date, addr, text))
    except Exception as e:
        pass




db_path = ''

for fn in os.listdir(db_path):
    iphone_db = os.path.join(db_path, fn)
    if is_message_table(iphone_db):
        try:
            print('[*] --- Found Messages ---')
            print_messages(iphone_db)
        except Exception as e:
            pass

for fn in os.listdir(os.getcwd()):
    print_tables(fn)
