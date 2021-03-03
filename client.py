import socket
from cryptography.fernet import Fernet
from tkinter import *

def write_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('crypto.key', 'rb').read()

def encrypt(filename, key):
    f = Fernet(key)


def login():
    logn = str(log.get()) + str(pas.get())
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    write_key()
    key = load_key()
    file = logn.encode() 
    encrypt(file, key)
    sock = socket.socket()
    sock.connect(('localhost', 4040))
    sock.send((file))
    sock.send((key))
    data = sock.recv(1024).decode()
    sock.close()
    if data == 'True':
            lbl.configure(text = 'Ur logged in')
            log.destroy()
            lbl1.destroy()
            pas.destroy()
            btn.destroy()


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



