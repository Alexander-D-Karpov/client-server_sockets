with open('ip.env', mode='r') as file:
    server_ip = file.read()
import socket
from tkinter import *
import sys
import cv2
import pickle
import numpy as np
import struct
from PIL import Image

def login():
    logn = str(log.get()) + str(pas.get())
    sock = socket.socket()
    sock.connect((server_ip, 4040))
    sock.send(logn.encode())
    data = sock.recv(1024).decode()
    sock.close()
    if data == 'True':
            lbl.configure(text = 'Ur logged in')
            log.destroy()
            lbl1.destroy()
            pas.destroy()
            btn.configure(text = 'Start streaming', command=start_stream)

def start_stream():
    sock = socket.socket()
    sock.connect((server_ip, 4040))
    check_data = 'True'
    sock.send(check_data.encode())
    sock.close()
    HOST = 'localhost'
    PORT = 7777
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    
    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')
    
    conn, addr = s.accept()
    
    data = b''
    payload_size = struct.calcsize("L")
    
    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
    
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
    
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
    
        frame=pickle.loads(frame_data)
        print(frame.size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Заголовок окна', frame)
        cv2.waitKey(10)


window = Tk()
window.geometry('400x250')
window.title("Client")
lbl = Label(window, text="Login")
lbl.grid(column=0, row=0)
log = Entry(window,width=10)  
log.grid(column=1, row=0)

lbl1 = Label(window, text="Password")
lbl1.grid(column=0, row=1)
pas = Entry(window,width=10)  
pas.grid(column=1, row=1)

btn = Button(window, text="Log in", command=login)  
btn.grid(column=0, row=3)  
window.mainloop()



