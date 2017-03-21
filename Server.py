import socket
import sys

class Server :
    host = 'localhost'
    port = 12800
    clients = []

    def __init__(self):
        try :
            con = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg :
            print "Failed"
            sys.exit()
        con.bind((self.host, self.port))
        con.listen( 5 )
        print( "this is connected on port {}".format(self.port))
        link, adress = con.accept()
        while true :
            data = link.recv(1024)
            if not data: break
            rep = "display : {}".format(data)
            print rep
            link.send(rep)
        link.close()

    def _get_client(self):
        return self.clients

server = Server()