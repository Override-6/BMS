from tkinter import *
from tkinter import font 
from tkinter import ttk

class MMI:

    def __init__(self):
        self.Window = Tk() 
        self.Window.withdraw() 
          
        
        self.login = Toplevel() 
        
        self.login.title("Connection") 
        self.login.resizable(width = False,  
                             height = False) 
        self.login.configure(width = 400, 
                             height = 400) 

        
        self.pls = Label(self.login,  
                       text = "Merci de vous connecter pour continuer", 
                       justify = CENTER,  
                       font = "Roboto 14 bold") 
          
        self.pls.place(relheight = 0.2, 
                       relx = 0.01,  
                       rely = 0.07) 
        
        self.labelName = Label(self.login, 
                               text = "Prenom: ", 
                               font = "Roboto 12") 
          
        self.labelName.place(relheight = 0.2, 
                             relx = 0.1,  
                             rely = 0.2) 
          
        
        
        self.entryName = Entry(self.login,  
                             font = "Roboto 14") 
          
        self.entryName.place(relwidth = 0.4,  
                             relheight = 0.12, 
                             relx = 0.35, 
                             rely = 0.2) 
          
        
        self.entryName.focus() 
          
        
        
        self.go = Button(self.login, 
                         text = "CONTINUER",  
                         font = "Roboto 14 bold",  
                         command = lambda: self.goAhead(self.entryName.get())) 
          
        self.go.place(relx = 0.4, 
                      rely = 0.55) 
        
        self.Window.mainloop()

m = MMI()