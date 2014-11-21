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
        rows = self.getDBinfo()
        theDict = self.fillLB(rows)
        
        
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
        self.fwdLabel = tk.Label(self, text = 'Forwarding Clients')
        
        self.infoLB = tk.Listbox(self, selectmode='single', width=70)
        

        #make entry boxes
        self.firstEntry = tk.Entry(self, width=40)
        self.lastEntry = tk.Entry(self, width=40)

        #display widgets in grid
        self.welcomeLabel.grid(row=0, column=0)
        self.searchLabel.grid(row=1, column=0)
        
        self.lastName.grid(row=3, column=2)
        self.lastEntry.grid(row=3, column=3)
        self.firstName.grid(row=3, column=0, sticky = 'e')
        self.firstEntry.grid(row=3, column=1)
        self.searchButton.grid(row=3, column=4)
        self.fwdLabel.grid(row=5, column=0, columnspan=2)
        
<<<<<<< HEAD
        self.infoLB.grid(row=6,column=0,columnspan=2)
        self.printButton.grid(row=5, column=3)
=======
        self.infoLB.grid(row=6,column=0,columnspan=3)
>>>>>>> 0f06de6a9c3b27eb9d25b984f2cae2e82c03f9bf

    def getDBinfo(self):    
        # Get a cursor object
        conn = sqlite3.connect('clientDB2.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT fname, lname, forwardingAddress, city,
                                        state, zipcode FROM client''')
                
        all_rows = cursor.fetchall()
        conn.close()
        
        return all_rows

    def fillLB(self, rows):
        self.infoLB.delete(0, 'end')
        
        for row in rows:
            self.infoLB.insert('end',
                '{1}, {0}: {2}, {3} {4} {5}'.format(row[0], row[1], row[2],
                                                    row[3], row[4], row[5]))

    def search(self):
        dataRows = self.getDBinfo()

        lname = self.lastEntry.get()
        fname = self.firstEntry.get()

        searchList = []

        if lname == '' and fname == '':
            tkMessageBox.showinfo('Error', 'Please enter first/last name.')
        else:
            for row in dataRows:
                #if first and last name are equal, append
                if fname == row[0] and lname == row[1]:
                    searchList.append(row)
                #if only first name is equal, append
                elif fname == row[0]:
                    searchList.append(row)
                #if only last name is equal, append
                elif lname == row[1]:
                    searchList.append(row)
            if searchList == []:
                tkMessageBox.showinfo('No Results', 'No matches found.')
                self.fillLB(dataRows)
            else:
                self.fillLB(searchList)       
        
    def printLabel(self):
        selected = self.infoLB.get('active')
        matchObj = re.match(r'([\w]+), ([\w]+): ([\w\s]+), ([\w\s]+)' ,
                                            selected, re.M|re.I)
        print matchObj.group(1)
        print matchObj.group(2)
        print matchObj.group(3)

        foo = {'name': matchObj.group(1) + ' ' + matchObj.group(2) , 'address': matchObj.group(4), 'state':matchObj.group(3)}
        test = labelCreator.labelMaker(foo)
        test.create_everything()
        
        

def main():
    app = Application()
    app.master.title('Mail Center Client GUI')
    app.master.geometry('800x300')
    app.mainloop()

if __name__ == '__main__':
    main()


