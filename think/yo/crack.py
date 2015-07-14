import crypt

# crypt produces diff answer each time

# use SHA-512 from hashlib library


def get_passwd(guess):
    # salt = guess[0:2]
    dict_file = open('words', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        # crypt_word = crypt.crypt(word, salt)
        crypt_word = crypt.crypt(word)
        if crypt_word == guess:
            return word


passwd_file = open('shadow-')
for line in passwd_file.readlines():
    if ":" in line:
        user = line.split(':')[0]
        crypt_passwd = line.split(':')[1].strip(' ')
        print('[*] Cracking Password For: %s' % user)
        passwd = get_passwd(crypt_passwd)
        if passwd:
            print('[+] Password Found: %s\n' % word)
            exit(0)
print('[-] Password Not Found.\n')
