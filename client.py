import socket
from tkinter import *
import json

def login():
    data = {
    "user_data": {
        "login": log.get(),
        "species": pas.get()
        }
    }
    sock = socket.socket()
    sock.connect(('localhost', 4040))
    with open('test_file.json', 'w') as file:
        json.dump(data, file)
    print(test_file.json)
    sock.send(test_file.json.encode())
    return_data = sock.recv(1024).decode()
    sock.close()
    if return_data == 'True':
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



