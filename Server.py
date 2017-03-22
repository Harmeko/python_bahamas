import socket
import select
import sys
import pprint

class Server :
    host = 'localhost'
    port = 12800
    clients = []
    sock = ""

    def __init__(self):
        try :
            self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg :
            print "Failed"
            sys.exit()
        self.sock.bind((self.host, self.port))
        self.sock.listen( 5 )
        print( "this is connected on port {}".format(self.port))
        self.clients = [self.sock]


    def run(self):
        while 1 :
            newsock = self.sock.accept()
            self.clients.append( newsock )
            # str = self.sock.recv(100)
            # pprint.pprint(str)
            # if str == "":
                # print "empty message"
                # self.sock.close
            # else:
            print "TEST"


    def _get_client(self):
        return self.clients

server = Server()
server.run()