from Network.MessageChannel import MessageChannel
import socket as sock
    def __init__(self, socket: sock.socket):
        self.socket = socket

    def send_message(self, message):
        self.socket.send(message)
        pass

    def on_message_received(self, message):
        print(message)
        pass
