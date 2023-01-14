import socket

print('Hello')
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 9000))
request = 'GET http://127.0.0.1/page1.htm HTTP/1.0\r\n\r\n'.encode()
my_socket.send(request)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

my_socket.close()

print('Socket closed')
