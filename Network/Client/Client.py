from Network.MessageChannel import MessageChannel

import socket as sock
from datetime import datetime

class Client(MessageChannel):
    """
    Classe du client, les messages sont envoyés en utilisant Client#sendMessage
    """

    def __init__(self, name, socket: sock.socket):
        super().__init__(socket)
        self.name = name

    def send_message(self, message: bytes):
        date = datetime.now().strftime("%H:%M:%S")
        complete_message = f"[{date}] {self.name} a dit : "
        super().send_message(bytes(complete_message, "UTF-8") + message)

    def on_message_received(self, message):
        """
        Le message est simplement print
        """
        message_str = str(message, "UTF-8")
        print(message_str, end='')
