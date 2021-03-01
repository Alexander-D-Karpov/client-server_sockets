import socket

sock = socket.socket()
sock.connect(('localhost', 8888))
sock.send('It is me, your best frind')

data = sock.recv(1024)
sock.close()

print(data)