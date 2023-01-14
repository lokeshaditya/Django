import urllib.request

req_hand = urllib.request.urlopen('http://127.0.0.1:9000/rom.txt')

for line in req_hand :
    print(line.decode())
    print(line.decode().strip())
