import socket as sock

from Network.Server.Server import Server

PORT = 48483

def start():
    serversocket = sock.socket()
    serversocket.bind(('', PORT))
    serversocket.listen(1)
    Server(serversocket)


if __name__ == '__main__':
    start()
