import socket
import os


class Server:
    def __init__(self, port=47):
        sp = socket.socketpair()
        pid = os.fork()
        if pid == 0:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(("", port))
            self.parent = sp[1]
        else:
            self.child = sp[0]
            self.pid = pid

    def block(self):
        pass


if __name__ == "__main__":
    server = Server()
    server.block()
