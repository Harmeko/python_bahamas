import socket
from tkinter import *

aff = Tk()
client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
host = client.gethostname()
port = 12800

client.connect((host, port))
data = client.recv(1024)
label = Label(aff, data)
label.pack
client.close()

aff.mainloop()