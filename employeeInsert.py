# New Mail Center Employee Insert
# Andrew Fenwick

import re
import Tkinter as tk
import tkMessageBox
import sqlite3
from dataBase import DataBase

DB = DataBase()

class employeeInsert(tk.Frame):
    def __init__(self, master=None):
        #create frame
        tk.Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

#Insert widgets
    def create_widgets(self):
        #instantiate the text box, labels, and button
        self.introLabel = tk.Label(self, text = 'Enter employee username')
        self.InsertUser = tk.Entry(self, width=40)
        self.saveButton = tk.Button(self, text = 'Enter', command = self.update)      
        self.UsernameLabel = tk.Label(self, text = 'Username')

        #display the text box, labels, and button
        self.introLabel.grid()
        self.UsernameLabel.grid(row = 1, column = 0)
        self.InsertUser.grid(row = 1, column = 1)
            
        self.saveButton.grid()

    def update(self):
        #run employee insert in dataBase.py and check if successful
        if DataBase.insert_employee(DB, self.InsertUser.get()) == True:
            #display success messageand empty text box
            tkMessageBox.showinfo('Username accepted', 'The username has been accepted.')
            self.InsertUser.delete(0, tk.END)
        elif DataBase.insert_employee(DB, self.InsertUser.get()) == False:
            #display failure message and empty text box
            tkMessageBox.showinfo('An error has occurred', 'The username could not be added to the database.')
            self.InsertUser.delete(0, tk.END)
        else:
            #display message if nothing was entered
            tkMessageBox.showinfo('No username given', 'Please enter a username first.')
        print self.InsertUser.get()      
    

def main():
    app = employeeInsert()
    app.master.title('Input Employee Username')
    app.master.geometry('%dx%d%+d%+d' % (400, 75, 300, 300))
    app.mainloop()

if __name__ == '__main__':
    main()
