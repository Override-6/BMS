import socket as sock

from Network.MessageChannel import MessageChannel
from Network.Server.Server import Server


class ServerConnection(MessageChannel):
    """
    Représente une des connections Serveur-Client.
    """
    def __init__(self, server: Server, socket: sock.socket):
        """
        :param server: Le serveur
        :param socket: le socket de la connection client-serveur
        """
        super().__init__(socket)
        self.server = server

    def on_message_received(self, message):
        print(str(message, "UTF-8"), end='')
        self.server.broadcast_message(self, message)

    def close(self):
        """
        Ferme la connection et se désenregistre du serveur.
        """
        super().close()
        self.server.unregister(self)

