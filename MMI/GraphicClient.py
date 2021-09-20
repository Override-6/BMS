from Network.Client.Client import Client


class GraphicClient(Client):
    def __init__(self, store, name, socket):
        super().__init__(name, socket)
        self.labels = store

    def on_message_received(self, message):
        self.labels.addMessage(message)

