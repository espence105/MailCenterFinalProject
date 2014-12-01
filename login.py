# LoginFrontEnd.py 
# Author: Eric Spence
# 10/11/14

import Tkinter as tk
from Tkinter import IntVar
import tkMessageBox
import ldapConnection
import dataBase
import mailCenterClientGui
import forwardClientGui
import newUser

from passlib.hash import sha256_crypt


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
        # Create button to create non-au login
        self.createNewUserButton = tk.Button(self,text='Create New Login', command = self.create_new_login)
        # Adds the widgets to the Tkinter frame
        self.introLabel.grid()
        self.userNameLabel.grid(row=1, column = 0)
        self.userName.grid(row=1,column=1)
        self.userPasswordLabel.grid(row=2,column=0)
        self.userPassword.grid(row=2,column=1)
        self.loginButton.grid(row=4, column = 0)
        self.createNewUserButton.grid(row=4,column =1)
    
        # Adding radio buttons to the login frame
        self.selection = IntVar() # IntVar is a Tkinter function to interact with radio Buttons
        self.mailCenterLogin = tk.Radiobutton(self, text='Employee', variable = self.selection, value=1).grid(row=3,column=0)
        self.studentLogin = tk.Radiobutton(self, text='Student', variable = self.selection, value=2).grid(row=3,column=1)
        self.nonAuLogin = tk.Radiobutton(self,text='NonAu Login', variable = self.selection, value=3).grid(row=3,column=2)
        
    # The action taken with the button click
    def login(self):
        if self.attempt_login():
            typePerson = self.selection.get()
            self.destroy()
            if(typePerson == 1):
               # Creating the mailCenterClientGui
               newGui = mailCenterClientGui.Application()
               newGui.master.title('Mail Center Client')
               newGui.master.geometry("800x300")
               newGui.mainloop()
              # Creates  
            if(typePerson == 2 or typePerson == 3):
               newGui = forwardClientGui.ClientFrontend()
               newGui.master.title('Mail Forwarding ')
               newGui.master.geometry("800x300")
               newGui.mainloop()
        else:
            tkMessageBox.showinfo('Incorrect Information', 'Your username or password is incorrect')
            
    # Attempts to login    
    def attempt_login(self):
        typePerson = self.selection.get()
        connection = ldapConnection.ldapConnection(self.userName.get(), self.userPassword.get())

        # This is for a mailcenter login
        if(typePerson == 1):
           if connection.connect():
               data = dataBase.DataBase()
               if data.select_employee(self.userName.get()):
                   return True
               else:
                   return False

        # Student/Facualty login     
        if(typePerson == 2):
            return connection.connect()
        
        # Non-Student login
        if(typePerson == 3):
            db = dataBase.DataBase()
            response = db.select_nonstudent(self.userName.get()) # Gets the username and hash of userpassword
            if response != None:
                if sha256_crypt.verify(self.userPassword.get(), response[1]): # Checks if password inputted and the one in db are the same
                    return True
                else:
                    return False
            
    def create_new_login(self):
        self.destroy()
        # Create a new frame to create a new user
        newUserFrame = newUser.Application()
        newUserFrame.master.title('Create a new User')
        newUserFrame.master.geometry("%dx%d%+d%+d" % (400, 150, 400, 400))
        newUserFrame.mainloop()
   
# Creates the GUI
def main():
    app = Application()
    app.master.title('Login')
    app.master.geometry("%dx%d%+d%+d" % (700, 150, 400, 400))
    app.mainloop()
    

if __name__ == '__main__':
    main()
