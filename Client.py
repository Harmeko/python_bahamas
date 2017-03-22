import socket
from Tkinter import *
import sys


class Client :
    sock = ""
    name = ""

    def __init__(self):
        aff = Tk()
        input_client = StringVar()
        input_field = Entry(aff, text=input_client)
        input_field.pack()
        frame = Frame(aff, width=400, height=400)
        frame.bind("<Return>", Send_Message)
        frame.pack()
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
        client.close()
        aff.mainloop()

    def _set_name(self, name):
        self.name = name
    def _get_name(self):
        return self.name

def Send_Message(event):
    print input_field.get()

client = Client()