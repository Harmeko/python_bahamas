import socket
from Tkinter import *
import sys
import cv2
import threading
from PIL import Image
from PIL import ImageTk

# def getVideo(self, aff):
#         cv2.namedWindow("preview")
#         vc = cv2.VideoCapture(0)

#         if vc.isOpened(): # try to get the first frame
#             rval, frame = vc.read()
#         else:
#             rval = False

#         while rval:
#             cam = Label(aff, image=frame)
#             cam.pack()
#             rval, frame = vc.read()
#             key = cv2.waitKey(20)
#             if key == 27: # exit on ESC
#                 break
#         cv2.destroyWindow("preview")

class Client :
    sock = ""
    name = ""
    input_field = ""
    vs = ""
    stopEvent = ""
    panel = ""
    frame = ""

    def __init__(self, vs):
        self.vs = vs
        self.stopEvent = None
        self.panel = None
        aff = Tk()
        self.frame = Frame(aff, width=400, height=400)

        input_client = StringVar()

        self.input_field = Entry(aff, text=input_client)
        self.input_field.pack()
        self.input_field.bind("<Return>", self.Send_Message)

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        self.frame.pack()
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
        # data = client.recv(1024)
        client.close()
        aff.mainloop()

    def _set_name(self, name):
        self.name = name
    def _get_name(self):
        return self.name

    def Send_Message(self, event):
        print self.input_field.get()
        return "break"

    def videoLoop(self):
        try:
            while not self.stopEvent.is_set():
                self.frame = self.vs.read()

                # image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                if self.panel is None:
                    self.panel = tki.Label(image=image)
                    self.panel.image = image
                    self.panel.pack(side="left", padx=10, pady=10)

                else:
                    self.panel.configure(image=image)
                    self.panel.image = image

        except RuntimeError, e:
            print("[INFO] caught a RuntimeError")

vc = cv2.VideoCapture(0)


client = Client(vc)