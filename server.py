import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import pyautogui
import time
from PIL import Image

sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    conn.close()
    if data:
        print(data.decode())
        if data.decode() == 'adminadmin':
            re_data = 'True'
            conn, addr = sock.accept()
            conn.send(re_data.encode())
            inf = conn.recv(1024).decode()
            conn.close()
            if inf == 'True':                 
                clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientsocket.connect(('localhost', 7777))
                while True:
                    image = pyautogui.screenshot()
                    image = image.resize((192, 108), Image.ANTIALIAS)
                    image = np.array(image)
                    img = Image.frombytes('RGB', (192, 108), image)
                    data = pickle.dumps(np.array(img))
                    clientsocket.sendall(struct.pack("L", len(data)) + data)

