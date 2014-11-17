# LoginFrontEnd.py 
# Author: Eric Spence
# 10/11/14

import Tkinter as tk
from Tkinter import IntVar
import tkMessageBox

class Application(tk.Frame):
    # Constructor 
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    # Adds all of the widgets to the frame  
    def create_widgets(self):
        self.introLabel = tk.Label(self, text='Please Enter UserName and Password')
        self.quitButton = tk.Button(self, text='Login', command = self.login)

        self.userName = tk.Entry(self, width=40)
        self.userName.insert(0,'UserName')

        self.userNameLabel = tk.Label(self, text='UserName')
        self.userPasswordLabel = tk.Label(self, text='Password')
        
        self.userPassword = tk.Entry(self, width=40, show='*')
        self.userPassword.insert(0,'***')
        
        self.introLabel.grid()
        self.userNameLabel.grid(row=1, column = 0)
        self.userName.grid(row=1,column=1)

        self.userPasswordLabel.grid(row=2,column=0)
        self.userPassword.grid(row=2,column=1)
        self.quitButton.grid(row=4)

        self.selection = IntVar()
        self.mailCenterLogin = tk.Radiobutton(self, text='Employee', variable = self.selection, value=1).grid(row=3,column=0)
        self.studentLogin = tk.Radiobutton(self, text='Student', variable = self.selection, value=2).grid(row=3,column=1)
        
    # The action taken with the button click
    def login(self):
        if self.attempt_login():
            pass
        else:
            tkMessageBox.showinfo('Incorrect Information', 'Your username or password is incorrect')
    # Attempts to login    
    def attempt_login(self):
        typePerson = self.selection.get()
        if(typePerson == 1):
            pass
        if(typePerson == 2):
            pass
        return False
   
        
        

def main():
    app = Application()
    app.master.title('Login')
    app.master.geometry("%dx%d%+d%+d" % (500, 150, 400, 400))
    app.mainloop()
    

if __name__ == '__main__':
    main()
