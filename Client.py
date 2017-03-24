import socket
import uuid
from Tkinter import *
import sys
import cv2
import threading
from PIL import Image
from PIL import ImageTk
import pprint
import json

HOST = 'localhost'
PORT = 12800

class Client :
    sock = ""
    name = ""
    input_field = ""
    vs = ""
    stopEvent = ""
    panel = ""
    frame = ""
    activeChan = ""
    channels = []
    ip = ""
    uid = ""

    def __init__(self, vs):
        self.vs = vs
        self.uid = uuid.uuid4()
        self.stopEvent = None
        self.panel = None
        aff = Tk()
        self.frame = Frame(aff, width=200, height=50)

        input_client = StringVar()

        self.input_field = Entry(aff, text=input_client)
        self.input_field.pack()
        self.input_field.bind("<Return>", self.Send_Message)

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        self.frame.pack()

        self.connectServer()

        self.sock.send("/list")

        clients = self.sock.recv(1024)

        pprint.pprint( json.loads(clients) )

        aff.mainloop()

    def _set_name(self, name):
        self.name = name
    def _get_name(self):
        return self.name

    def Send_Message(self, event):
        currsock = self.sock

        str = self.input_field.get()
        pprint.pprint(self.sock)
        print str
        try :
            currsock.send(str)
            test = currsock.recv(1024)
        except Exception as er:
            pprint.pprint(er)
        # currsock.close()

    def connectServer(self):
        try :
            self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg :
            print "Failed"
            sys.exit()
        self.ip = socket.gethostbyname( HOST )
        # data = client.recv(1024)
        try:
            self.sock.connect((self.ip, PORT))
        except Exception as e:
            pprint.pprint(e)

    def videoLoop(self):
        try:
            while not self.stopEvent.is_set():
                self.frame = self.vs.read()[1]
                key = cv2.waitKey(20)
                # # pprint.pprint(self.frame)
                # image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # # image = cv2.resize(image, (500, 500))
                # image = Image.fromarray(image[1])
                # # image = image.resize((250, 250))
                # image = ImageTk.PhotoImage(image)

                # if self.panel is None:
                #     self.panel = Label(image=image, width=400, height=400)
                #     self.panel.image = image
                #     self.panel.pack(side="left")
                # else:
                #     self.panel.configure(image=image)
                #     self.panel.image = image
                cv2.imshow("test", self.frame)

        except RuntimeError, e:
            print("[INFO] caught a RuntimeError")

    def getChannels(self):
        try:
            self.sock.send("\o/getChannels")
        except:
            print "ERROR: CODE 7070, useless dev."


vc = cv2.VideoCapture(0)
vc.set(3, 500)
vc.set(4, 500)

client = Client(vc)
