import SocketServer
import select
import sys
import pprint

# host = 'localhost'
# port = 12800
class Server(SocketServer.BaseRequestHandler):
    clients = []
    sock = ""
    data = ""
    request = None


    # def __init__(self):
    #     self.request = request
    #     self.handle()
        # try :
        #     self.sock = SocketServer.TCPServer( self.host, self.port)
        # except:
        #     print "Failed"
        #     sys.exit()
        # self.sock.bind((self.host, self.port))
        # self.sock.listen( 5 )
        # print( "this is connected on port {}".format(self.port))
        # self.clients = [self.sock]

    def handle(self):
        readsock = select.select(self.clients, [], [])
        for sock in readsock:
            pprint.pprint(sock)
            if sock == self.clients[0]:
                self.clients.append( self.request )
            else:
                try:
                    self.data = self.request.recv(100).strip()
                    pprint.pprint(self.data)
                    self.request.send(self.data)
                except Exeption as e:
                    print e


if __name__ == "__main__":
    HOST, PORT = "localhost", 12800
    # def run(self):
    #     while 1 :
    #         readsock = select.select(self.clients, [], [])
    #         for sock in readsock:
    #             pprint.pprint(sock)
    #             if sock == self.clients[0]:
    #                 newsock, newaddr = self.sock.accept()
    #                 self.clients.append( newsock )
    #             else:
    #                 try:
    #                     data = sock.recv(100)[0]
    #                     if data:
    #                         pprint.pprint(data)
    #                 except:
    #                     print "Client is offline"
    #                     # sock.close()
    #                     continue
    #         # str = newsock.recvfrom(100)[0]
    #         pprint.pprint(str)
    #         #coucou
    #         # if str == "":
    #             # print "empty message"
    #             # self.sock.close
    #         # else:
    #         print "TEST"


    # def _get_client(self):
    #     return self.clients

server = SocketServer.TCPServer( ( HOST, PORT ), Server )
server.serve_forever()