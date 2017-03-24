import SocketServer
import select
import sys
import pprint
import json

# host = 'localhost'
# port = 12800
class Server(SocketServer.BaseRequestHandler):
    clients = []
    sock = ""
    data = ""
    request = None


    def __init__(self, request, client_address, server):
        pprint.pprint(request)
        pprint.pprint(client_address)
        self.clients.append( client_address )
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return
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
        pprint.pprint(self.clients)
        while self.data != 0:
            self.data = self.request.recv(100).strip()
            if self.data == "/list":
                self.request.send( json.dumps(self.clients) )
            else :
                self.request.send(self.data)
            
            pprint.pprint(self.data)
            # if self.data == "/list"
            #     for i in self.clients

                # return self.request.send(listclients)



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