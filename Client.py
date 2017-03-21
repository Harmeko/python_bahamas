import socket
from Tkinter import *


class Client :
    sock = ""
    name = ""

    def __init__(self):
        aff = Tk()
        self.sock, client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 12800
        client.connect((host, port))
        data = client.recv(1024)
        label = Label(aff, "TEST")
        label.pack
        client.close()
        aff.mainloop()

    def _set_name(self, name):
        self.name = name
    def _get_name(self):
        return self.name

client = Client()