with open('ip.env', mode='r') as file:
    server_ip = file.read()
from socket import socket
from tkinter import *

def login():
    logn = str(log.get()) + str(pas.get())
    sock = socket.socket()
    sock.connect((server_ip, 4040))
    sock.send(logn.encode())
    data = sock.recv(1024).decode()
    sock.close()
    if data == 'True':
            lbl.configure(text = 'Ur logged in')
            msg = ("Hello you there!").encode('utf-8')
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



