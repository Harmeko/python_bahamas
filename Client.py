import socket
from Tkinter import *
import sys


class Client :
    sock = ""
    name = ""

    def __init__(self):
        aff = Tk()
        try :
            client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg :
            print "Failed"
            sys.exit()
        host = 'localhost'
        port = 12800
        try :
            ip = socket.gethostbyname( host )
            self.sock = ip
        except socket.gaierror:
            print "Hostname not resolve exit"
            sys.exit()
        client.connect((ip, port))
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