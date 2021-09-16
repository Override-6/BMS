from Network.MessageChannel import MessageChannel
import socket as sock

class Server(MessageChannel):
    def __init__(self, socket: sock.socket):
        self.socket = socket

    def start(self):
