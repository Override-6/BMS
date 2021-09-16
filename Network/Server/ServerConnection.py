from Network.Server.Server import Server
import threading
import socket as sock

BUFF_SIZE = 2024

class ServerConnection:
    def __init__(self, socket: sock.socket):
        self.socket = socket

    def message_loop(self):
        while True:
            message = self.socket.recv(BUFF_SIZE)

    def start(self):
        threading.Thread(target=self.message_loop).start()
