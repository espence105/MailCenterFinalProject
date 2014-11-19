# LoginFrontEnd.py 
# Author: Eric Spence
# 10/11/14

import Tkinter as tk
from Tkinter import IntVar
import tkMessageBox

class Application(tk.Frame):
    """
     Used to create the Gui for the Login

     This creates a gui with Instructions for the user. It has to entry widgets
     for username and password. Password will show up as ****

     Attributes:
         master : Defaults to None
    """
    # Constructor - Creates the frame
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    # Adds all of the widgets to the frame  
    def create_widgets(self):
        # Creating the Intro Label
        self.introLabel = tk.Label(self, text='Please Enter UserName and Password')
        # Creating the login Button
        self.loginButton = tk.Button(self, text='Login', command = self.login)
        # Creating userName entry widget and populating it with 'User Name' 
        self.userName = tk.Entry(self, width=40)
        self.userName.insert(0,'User Name')
        # Creating labels that say User Name and Password
        self.userNameLabel = tk.Label(self, text='User Name')
        self.userPasswordLabel = tk.Label(self, text='Password')
        # Creating an entry widget for password that will show ****
        self.userPassword = tk.Entry(self, width=40, show='*')
        self.userPassword.insert(0,'***')
        # Adds the widgets to the Tkinter frame
        self.introLabel.grid()
        self.userNameLabel.grid(row=1, column = 0)
        self.userName.grid(row=1,column=1)
        self.userPasswordLabel.grid(row=2,column=0)
        self.userPassword.grid(row=2,column=1)
        self.loginButton.grid(row=4)
        # Adding radio buttons to the login frame
        self.selection = IntVar() # IntVar is a Tkinter function to interact with radio Buttons
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
   
# Creates the GUI
def main():
    app = Application()
    app.master.title('Login')
    app.master.geometry("%dx%d%+d%+d" % (500, 150, 400, 400))
    app.mainloop()
    

if __name__ == '__main__':
    main()
