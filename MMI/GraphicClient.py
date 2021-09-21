from tkinter import END, DISABLED, NORMAL

from Network.Client.Client import Client


class GraphicClient(Client):
    def __init__(self, store, name, socket):
        super().__init__(name, socket)
        self.labels = store

    def pushMessage(self, message):
        self.labels.config(state=NORMAL)
        self.labels.insert(END, message)

        self.labels.config(state=DISABLED)
        self.labels.see(END)

    def send_message(self, message: bytes):
        print("Envoyé: " + str(message, "UTF-8"))
        super().send_message(message)

    def on_message_received(self, message):
        message = str(message, "UTF-8")
        print("Recu: " + message)
        self.pushMessage(message)

