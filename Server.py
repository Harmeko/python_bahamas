import socket
import select
import sys

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
            (read, write, exc) = select.select( self.clients, [], [] )

            for sock in read:
                if sock == self.sock:
                    newsock = self.sock.accept()
                    self.clients.append( newsock )
                else:
                    str = sock.recv(100)
                    if str == "":
                        print "empty message"
                        sock.close
                    else:
                        print "Not Empty Value"


    def _get_client(self):
        return self.clients

server = Server()