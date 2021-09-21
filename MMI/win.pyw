import socket as sock
from tkinter import *
import threading

from MMI.GraphicClient import GraphicClient
from Network.Client.Client import Client
from Network.MessageChannel import MessageChannel

IP = "127.0.0.1"
PORT = 48483
ADDRESS = (IP, PORT)
FORMAT = "utf-8"

class MMI:

    def __init__(self):
        #création de la fenêtre tkinter
        self.Window = Tk()
        self.Window.withdraw()
        #création widget (interaction avec l'utilisateur)
        self.login = Toplevel()
        #paramettre de la fenêtre
        self.login.title("Connection")
        #taille non-changeable
        self.login.resizable(width=False,
                             height=False)
        #taille définie
        self.login.configure(width=400,
                             height=400)
        #création du texte
        self.pls = Label(self.login,
                         text="Merci de vous connecter pour continuer",
                         justify=CENTER,
                         font="Roboto 14 bold")
        #placement dans la fenêtre
        self.pls.place(relheight=0.2,
                       relx=0.01,
                       rely=0.07)

        self.labelName = Label(self.login,
                               text="Prenom: ",
                               font="Roboto 12")

        self.labelName.place(relheight=0.2,
                             relx=0.1,
                             rely=0.2)

        self.entryName = Entry(self.login,
                               font="Roboto 14")

        self.entryName.place(relwidth=0.4,
                             relheight=0.12,
                             relx=0.35,
                             rely=0.2)

        self.entryName.focus()

        self.go = Button(self.login,
                         text="CONTINUE",
                         font="Helvetica 14 bold",
                         command=lambda: self.goAhead(self.entryName.get()))

        self.go.place(relx=0.4,
                      rely=0.55)
        self.client = None
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)

    def getname(self) -> str:
            return self.entryName.get()


    def layout(self, name):
            self.name = name

            self.Window.deiconify()
            self.Window.title("CHATROOM")
            self.Window.resizable(width=False,
                                  height=False)
            self.Window.configure(width=470,
                                  height=550,
                                  bg="#17202A")
            self.labelHead = Label(self.Window,
                                   bg="#17202A",
                                   fg="#EAECEE",
                                   text=self.name,
                                   font="Helvetica 13 bold",
                                   pady=5)

            self.labelHead.place(relwidth=1)
            self.line = Label(self.Window,
                              width=450,
                              bg="#ABB2B9")

            self.line.place(relwidth=1,
                            rely=0.07,
                            relheight=0.012)

            self.textCons = Text(self.Window,
                                 width=20,
                                 height=2,
                                 bg="#17202A",
                                 fg="#EAECEE",
                                 font="Helvetica 14",
                                 padx=5,
                                 pady=5)

            self.textCons.place(relheight=0.745,
                                relwidth=1,
                                rely=0.08)

            self.labelBottom = Label(self.Window,
                                     bg="#ABB2B9",
                                     height=80)

            self.labelBottom.place(relwidth=1,
                                   rely=0.825)

            self.entryMsg = Entry(self.labelBottom,
                                  bg="#2C3E50",
                                  fg="#EAECEE",
                                  font="Helvetica 13")

            self.entryMsg.place(relwidth=0.74,
                                relheight=0.06,
                                rely=0.008,
                                relx=0.011)

            self.entryMsg.focus()

            self.buttonMsg = Button(self.labelBottom,
                                    text="Send",
                                    font="Helvetica 10 bold",
                                    width=20,
                                    bg="#ABB2B9",
                                    command=lambda: self.sendButton(self.client, self.entryMsg.get()))

            self.buttonMsg.place(relx=0.77,
                                 rely=0.008,
                                 relheight=0.06,
                                 relwidth=0.22)

            self.textCons.config(cursor="arrow")

            scrollbar = Scrollbar(self.textCons)

            scrollbar.place(relheight=1,
                            relx=0.974)

            scrollbar.config(command=self.textCons.yview)

            self.textCons.config(state=DISABLED)

            socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            socket.connect((IP, PORT))
            self.client = GraphicClient(self.textCons, name, socket)

    def pushMessage(self, message):
        self.textCons.config(state=NORMAL)
        self.textCons.insert(END, message + "\n")

        self.textCons.config(state=DISABLED)
        self.textCons.see(END)

    def sendButton(self, channel: MessageChannel, msg):
        self.textCons.config(state = DISABLED)
        self.entryMsg.delete(0, END)
        msg = bytes(msg, "UTF-8")
        channel.send_message(msg)
        self.pushMessage(str(Client.format_message(msg, self.name), "UTF-8"))




if __name__ == '__main__':
    m = MMI()
    print(m.getname())

