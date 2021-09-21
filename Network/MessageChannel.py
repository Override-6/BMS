import socket as sock
from threading import Thread

BUFF_SIZE = 2048


class MessageChannel:

    def __init__(self, socket: sock.socket):
        """
        :param socket: Le socket de ce message channel pour envoyer et recevoir les messages.
        """
        self.socket = socket
        self.listen = True
        # Création d'un thread dédié à la réception des messages du socket.
        Thread(target=self.__loop).start()

    @staticmethod
    def __remove_trailing_crlf(seq):
        """
        Enlève les deriniers charactères de nouvelle ligne ('_\n')
        :param seq: la séquence de charactère (bytes ou str) à modifier
        :return: la nouvelle séquence qui ne comporte plus de LineFeeds de fin.
        """
        while seq.endswith(b"\n"):
            seq = seq[0:len(seq) - 1]
        return seq

    def send_message(self, message: bytes):
        """
        envoie un message dans le socket
        :param message: Le message à envoyer
        """
        message = MessageChannel.__remove_trailing_crlf(message)
        self.socket.send(message + b"\n")

    # Méthode "abstraite", gère la reception d'un message
    def on_message_received(self, message):
        pass

    def close(self):
        self.listen = False
        self.socket.close()

    def __loop(self):
        """
        Méthode privée
        Se charge d'écouter les messages recu par le socket indéfiniment
        Cette méthode doit être lancée dans un nouveau thread.
        """
        try:
            while True:
                message = self.socket.recv(BUFF_SIZE)
                self.on_message_received(message)
        except:
            self.close()
            raise
