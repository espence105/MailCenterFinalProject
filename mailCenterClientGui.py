#mailCenterClientGui.py
#Makenzie Bontrager
#November 11

import Tkinter as tk
import tkMessageBox
import sqlite3
conn = sqlite3.connect('clientDB2.db')

class Application(tk.Frame):
    
    clientDictionary = {}

    def __init__ (self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        theDict = self.getDBinfo()
        self.create_table(theDict)
        self.create_widgets()
        
        
    def create_widgets(self):
        #make info labels
        self.welcomeLabel = tk.Label(self, text = 'Welcome Mail Center Client')
        self.searchLabel = tk.Label(self, text = 'Search for forwarding student')

        #make search button
        self.searchButton = tk.Button(self, text= 'Search', command = self.search)
        
        #make search info labels
        self.lastName = tk.Label(self, text = 'Last Name:') 
        self.firstName = tk.Label(self, text = 'First Name:')

        self.infoLB = tk.Listbox(self)

        #make entry boxes
        self.firstEntry = tk.Entry(self, width=40)
        self.firstEntry.insert(0, 'First Name')
        self.lastEntry = tk.Entry(self, width=40)
        self.lastEntry.insert(0, 'Last Name')

        #plop things in grid
        self.welcomeLabel.grid(row=0, column=0)
        self.searchLabel.grid(row=1, column=0)
        
        self.lastName.grid(row=3, column=0)
        self.lastEntry.grid(row=3, column=1)
        self.firstName.grid(row=3, column=2)
        self.firstEntry.grid(row=3, column=3)
        self.searchButton.grid(row=3, column=4)
        
##        self.infoLB.grid(row=4,column=1)

    def getDBinfo(self):    
        # Get a cursor object
        cursor = conn.cursor()

        cursor.execute('''SELECT fname, lname FROM client''')
                
        all_rows = cursor.fetchall()
        
        for row in all_rows:
            clientDictionary = {row[0]:row[1]}
            return clientDictionary
##            self.infoLB.insert(0, 'first name: {0} last name: {1}'.format(row[0], row[1]))

            
        
    def create_table(self, dictionary):
        
        rows = []
        for i in range(4, len(dictionary)+4):
            cols = []
            for j in range(4):
                self.e = tk.Entry(self)
                self.e.grid(row=i, column=j)
                cols.append(self.e)
            rows.append(cols)

    def search(self):
        pass       



def main():
    app = Application()
    app.master.title('Mail Center Client GUI')
    app.mainloop()

if __name__ == '__main__':
    main()


