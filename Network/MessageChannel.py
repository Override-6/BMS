import socket as sock
from threading import Thread

BUFF_SIZE = 2048


class MessageChannel:

    def __init__(self, socket: sock.socket):
        self.socket = socket
        self.listen = True
        # Création d'un thread dédié à la réception des messages du socket.
        Thread(target=self.__loop).start()

    @staticmethod
    def __remove_trailing_crlf(seq):
        while seq.endswith(b"\n"):
            seq = seq[0:len(seq) - 2]
        return seq

    def send_message(self, message: bytes):
        message = MessageChannel.__remove_trailing_crlf(message)
        self.socket.send(message + b"\n")

    # Méthode "abstraite", gère la reception d'un message
    def on_message_received(self, message):
        pass

    def close(self):
        self.listen = False
        self.socket.close()

    def __loop(self):
        try:
            while self.listen:
                message = self.socket.recv(BUFF_SIZE)
                self.on_message_received(message)
        except:
            self.close()
            # raise
