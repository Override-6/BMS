from datetime import datetime

from Network.Client.Client import Client
import socket as sock

print("Bienvenue dans la messagerie hyper sofistiquée de Maxime et l'autre")

IP = "127.0.0.1"
PORT = 48483

def start():
    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    print("Connection à", IP, " sur le port", PORT, "...")
    socket.connect((IP, PORT))
    name = input("Insérez un pseudo :")
    client = Client(name, socket)
    print("Le client a démarré, début de la discution !", flush=True)
    socket.send(str.encode(name + " s'est connecté.\n", "UTF-8"))
    while True:
        message = input()
        client.send_message(bytes(message, "UTF-8"))
        date = datetime.now().strftime("%H:%M:%S")
        print(f"[{date}] Vous avez envoyé : " + message)


if __name__ == '__main__':
    start()
