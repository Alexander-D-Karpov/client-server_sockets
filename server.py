import socket

sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    if data:
        print(data.decode())
        if data.decode() == 'adminadmin':
            re_data = 'True'
            conn.send(re_data.encode())
        conn.close()

