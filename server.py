import socket
from cryptography.fernet import Fernet
import sqlite3
import rsa

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

conn_sql = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn_sql.cursor()

sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    if data:
        file = data.decode()
        data = conn.recv(1024)
        key = data.decode()
        decrypt(file, key)
        print(data.decode())
        if data.decode() == 'adminadmin':
            re_data = 'True'
            conn.send(re_data.encode())
        conn.close()

conn_sql.close()