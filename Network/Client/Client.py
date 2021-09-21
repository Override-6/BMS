from Network.MessageChannel import MessageChannel

import socket as sock
from datetime import datetime


class Client(MessageChannel):
    """
    Classe du client, les messages sont envoyés en utilisant Client#sendMessage
    """

    def __init__(self, name, socket: sock.socket):
        """
        :param name: Le nom du client sur la messagerie
        :param socket: Le socket du client.
        """
        super().__init__(socket)
        self.name = name

    @staticmethod
    def format_message(message: bytes, name) -> bytes:
        """
        :param message: Le message à formatter
        :param name: Le nom du propriétaire du message
        :return:
        """
        date = datetime.now().strftime("%H:%M:%S")
        complete_message = f"[{date}] {name} a dit : "
        return bytes(complete_message, "UTF-8") + message

    def _send_message_no_format(self, message: bytes):
        """
        envoie un message sans le formater
        :param message: le message brut
        :return:
        """
        super().send_message(message)

    def send_message(self, message: bytes):
        """
        Envoie un message en le formattant
        :param message: le message brut.
        :return:
        """
        self._send_message_no_format(Client.format_message(message, self.name))

    def on_message_received(self, message):
        """
        Le message est simplement print
        """
        message_str = str(message, "UTF-8")
        print(message_str, end='')
