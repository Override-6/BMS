from Network.MessageChannel import MessageChannel

import socket as sock


class Client(MessageChannel):
    """
    Classe du client, les messages sont envoyés en utilisant Client#sendMessage
    """

    def __init__(self, name, socket: sock.socket):
        super().__init__(socket)
        self.name = name

    def send_message(self, message: bytes):
        super().send_message(bytes(self.name, "UTF-8") + b" a dit : " + message)

    def on_message_received(self, message):
        """
        Le message est simplement print
        """
        message_str = str(message, "UTF-8")
        print(message_str, end='')
