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

    @staticmethod
    def format_message(message: bytes, name) -> bytes:
        date = datetime.now().strftime("%H:%M:%S")
        complete_message = f"[{date}] {name} a dit : "
        return bytes(complete_message, "UTF-8") + message

    def _send_message_no_format(self, message: bytes):
        super().send_message(message)

    def send_message(self, message: bytes):
        self._send_message_no_format(Client.format_message(message, self.name))

    def on_message_received(self, message):
        """
        Le message est simplement print
        """
        message_str = str(message, "UTF-8")
        print(message_str, end='')
