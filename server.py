import socket
sock = socket.socket()
sock.bind(('', 8888))
sock.listen(1)
conn, adr = sock.accept()

print('Look at this boy, who connected: ' + str(adr))

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper)

conn.close()