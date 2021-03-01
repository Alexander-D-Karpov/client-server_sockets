import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    if data:
        data_str = data.decode()
        conn.send(data_str.upper().encode())
        conn.close()
        if data_str == 'stop':
            break
