import Tkinter as tk
from Tkinter import IntVar
import tkMessageBox
import dataBase
import login
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
        # Creating labels that say First Name and entry to put it
        self.userFirstName = tk.Entry(self, width=40)
        self.userFirstName.insert(0,'First Name')
        
        # Creating labels that say Last Name and entry to put it
        self.userLastName = tk.Entry(self, width=40)
        self.userLastName.insert(0,'Last Name')
        
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
        self.createNewUserButton = tk.Button(self,text='Create New Login', command = self.create_new_user)

        # Adds the widgets to the Tkinter frame
        self.userFirstName.grid(row=0,column=1)
        self.userLastName.grid(row=1,column=1)
          
        self.userNameLabel.grid(row=2, column = 0)
        self.userName.grid(row=2,column=1)
        self.userPasswordLabel.grid(row=3,column=0)
        self.userPassword.grid(row=3,column=1)
        
        self.createNewUserButton.grid(row=4,column =1)
    # Creates a new user in the database
    def create_new_user(self):
        # Hashes the password so that it is not stored in plan text in the db
        hash = sha256_crypt.encrypt(self.userPassword.get()) 
        # A new database
        db = dataBase.DataBase() 
        db.insert_nonstudent((self.userName.get(), hash, self.userFirstName.get(), self.userLastName.get()))
        # Destroys the current form
        self.destroy()
        
        # Creates new Login Form to login 
        app = login.Application()
        app.master.title('Login')
        app.master.geometry("%dx%d%+d%+d" % (700, 150, 400, 400))
        app.mainloop()
 
# Creates the GUI
def main():
    app = Application()
    app.master.title('Create a new User')
    app.master.geometry("%dx%d%+d%+d" % (400, 150, 400, 400))
    app.mainloop()
    
if __name__ == '__main__':
    main()
