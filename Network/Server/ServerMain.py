import socket as sock
PORT = 48483
def start():
    serversocket = sock.socket()
    serversocket.bind(('', PORT))
    serversocket.listen(1)
    serversocket

if __name__ == '__main__':
    start()