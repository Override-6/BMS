import socket as sock

from Network.MessageChannel import MessageChannel
from Network.Server.Server import Server


class ServerConnection(MessageChannel):
    def __init__(self, server: Server, socket: sock.socket):
        super().__init__(socket)
        self.server = server

    def on_message_received(self, message):
        print(str(message, "UTF-8"), end='')
        self.server.broadcast_message(self, message)
