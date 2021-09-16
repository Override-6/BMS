import socket as sock
from threading import Thread
from typing import List


class Server:
    def __init__(self, serversocket: sock.socket):
        from Network.Server.ServerConnection import ServerConnection

        self.serversocket = serversocket
        self.accept_connections = True
        self.connections: List[ServerConnection] = []
        self.messages = []
        # démare le serveur
        Thread(target=self.__connection_loop).start()

    def unregister(self, connection):
        self.connections.remove(connection)
        msg = f"Une connection s'est terminée."
        print(msg)  # Print sur le serveur
        self.broadcast_message(connection, bytes(msg, "UTF-8"))  # pour les autres

    def broadcast_message(self, sender, message):
        """
        diffuse un message à tout les clients connectés au serveur.
        :param sender: le ServerConnection qui broadcast le message.
        :param message: le message à diffuser
        """
        # Le message est gardé pour faire en sorte que les connections qui arrivent en cours de route
        # puissent avoir le reste de la discution.
        self.messages.append(message)
        # On itère sur chaque connections,
        # puis on envoie le message à tout les clients sauf le sender
        for connection in self.connections:
            if connection is not sender:
                connection.send_message(message)

    def handle_new_connection(self, client_socket):
        """
        Gère un nouveau client.
        le socket et "wrappé" dans un ServerConnection,
         puis il est mit dans la liste des connections du serveur
        :param client_socket: le socket du client qui vient de se connecter.
        """
        from Network.Server.ServerConnection import ServerConnection

        connection = ServerConnection(self, client_socket)  # On wrap le socket du client dans un ServerConnection
        self.connections.append(connection)  # On ajoute la connection dans la liste des connections du serveur.
        for message in self.messages:
            connection.send_message(message)

    def __connection_loop(self):
        """
        boucle infinie tant que le serveur n'est pas close.
        cette boucle accepte les connections au serveur.
        """
        while self.accept_connections:
            print("Socket Loop -> En attente du prochain client...")
            client_socket, address = self.serversocket.accept()  # On accepte le prochain client, renvoie un tuple (Socket, Adress)
            print("Socket Loop -> Nouveau client connecté :", client_socket)
            self.handle_new_connection(client_socket)
