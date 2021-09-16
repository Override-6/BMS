from Network.Client.Client import Client
import socket as sock

print("Bienvenue dans la messagerie hyper sofistiquée de Maxime et l'autre")

IP = "127.0.0.1"
PORT = 48483

BUFF_SIZE = 2048


def start():
    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    print("Connection à", IP, " sur le port", PORT, "...")
    socket.connect((IP, PORT))
    client = Client(socket, socket)
    print("Le client a démarré, début de la discution !")

    while (True):
        message = socket.recv(BUFF_SIZE)
        client.on_message_received(message)


if __name__ == '__main__':
    start()
