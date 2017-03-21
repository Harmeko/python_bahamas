import socket

host = ''
port = 12800

con = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
con.bind((host, port))
con.listen( 5 )
print( "this is connected on port {}".format(port))

link, adress = con.accept()
while true :
    data = link.recv(1024)
    if not data: break
    print "display : {}".format(data)
    link.send(data)
link.close()