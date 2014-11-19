#mailCenterClientGui.py
#Makenzie Bontrager
#November 11

import re
import labelCreator
import Tkinter as tk
import tkMessageBox
import sqlite3
conn = sqlite3.connect('clientDB2.db')

class Application(tk.Frame):
    
    def __init__ (self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        theDict = self.getDBinfo()
        
        
    def create_widgets(self):
        #make info labels
        self.welcomeLabel = tk.Label(self, text = 'Welcome Mail Center Client')
        self.searchLabel = tk.Label(self, text = 'Search for forwarding student')
        self.infoLB = tk.Listbox(self, selectmode='multiple', width=70)
        
        #make buttons
        self.searchButton = tk.Button(self, text= 'Search',
                                      command = self.search)
        self.printButton = tk.Button(self, text = 'Print Selected Labels',
                                     command = self.printLabel)
        
        #make search info labels
        self.lastName = tk.Label(self, text = 'Last Name:') 
        self.firstName = tk.Label(self, text = 'First Name:')

        self.infoLB = tk.Listbox(self, selectmode='single', width=70)
        

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
        
        self.infoLB.grid(row=4,column=0,columnspan=2)
        self.printButton.grid(row=4, column=3)

    def getDBinfo(self):    
        # Get a cursor object
        cursor = conn.cursor()

        cursor.execute('''SELECT fname, lname, forwardingAddress, city,
                                        state, zipcode FROM client''')
                
        all_rows = cursor.fetchall()
 
        clientDictionary = {}

        for row in all_rows:
            clientDictionary[row[0]]=(row[1],row[2])
            #clientDictionary['Last Name']= row[1]
            self.infoLB.insert('end',
                '{1}, {0}: {2}, {3} {4} {5}'.format(row[0], row[1], row[2],
                                                    row[3], row[4], row[5]))

    def search(self):
        pass
    
    def printLabel(self):
        selected = self.infoLB.get('active')
        matchObj = re.match(r'([\w]+), ([\w]+): ([\w\s]+), ([\w\s]+)' ,selected, re.M|re.I)
        print matchObj.group(1)
        print matchObj.group(2)
        print matchObj.group(3)

        foo = {'name': matchObj.group(1) + ' ' + matchObj.group(2) , 'address': matchObj.group(4), 'state':matchObj.group(3)}
        test = labelCreator.labelMaker(foo)
        test.create_everything()
        print selected
        
        

def main():
    app = Application()
    app.master.title('Mail Center Client GUI')
    app.mainloop()

if __name__ == '__main__':
    main()


