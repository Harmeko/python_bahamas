class Users :
    sock = 0
    name = ""

    def __init__( self, sock, name ):
        self.sock = sock
        self.name = name

    def _get_sock(self):
        return self.sock

    def _set_sock(self, sock):
        self.sock = sock

    def _set_name(self, name):
        self.name = name

    def _get_name(self):
        return self.name

