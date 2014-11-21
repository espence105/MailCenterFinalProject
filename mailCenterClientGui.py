#mailCenterClientGui.py
#Makenzie Bontrager
#November 11
#create mail center interface

import re
import labelCreator
import Tkinter as tk
import tkMessageBox
import sqlite3
conn = sqlite3.connect('clientDB2.db')

class Application(tk.Frame):
    """Creates the interface for the mail center.

    Displayed after a mail center employee sucessfully logs into the system.
    From this interface the employee can view all forwarding students, print
    forwarding labels, and search for individual forwarding students.

    Attributes:
        welcomeLabel: information label
        searchLabel: information label
        infoLB: lisbox that displays information from database
        searchButton: command application to do search function
        printButton: command application to do print function
        lastName: information lable
        lastEntry: last name user entry box
        firstName: information label
        firstEntry: first name user entry box
        fwdLabel: information label
        rows: list of information retreived from database
    """
    
    def __init__ (self, master = None):
        """create tkinter frame, intialize program; instantiate grid,
        call function to create widgets; import database information through
        getDBinfo() function call; fill infoLB with data through function call
        to fillLB()"""
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        rows = self.getDBinfo()
        self.fillLB(rows)
        
        
    def create_widgets(self):
        """create each widget and place them in the grid"""
        
        #make info labels
        self.welcomeLabel = tk.Label(self, text = 'Welcome Mail Center Client')
        self.searchLabel = tk.Label(self, text = 'Search for forwarding student')
        self.infoLB = tk.Listbox(self, selectmode='multiple', width=70)
        
        #make search info labels
        self.lastName = tk.Label(self, text = 'Last Name:') 
        self.firstName = tk.Label(self, text = 'First Name:')
        self.fwdLabel = tk.Label(self, text = 'Forwarding Clients')

        #make listbox
        self.infoLB = tk.Listbox(self, selectmode='single', width=70)
        
        #make buttons
        self.searchButton = tk.Button(self, text= 'Search',
                                      command = self.search)
        self.printButton = tk.Button(self, text = 'Print Selected Labels',
                                     command = self.printLabel)        

        #make entry boxes
        self.firstEntry = tk.Entry(self, width=40)
        self.lastEntry = tk.Entry(self, width=40)

        #display widgets in grid
        self.welcomeLabel.grid(row=0, column=0)
        self.searchLabel.grid(row=1, column=0)
        self.lastName.grid(row=3, column=2)
        self.firstName.grid(row=3, column=0, sticky = 'e')
        self.fwdLabel.grid(row=5, column=0, columnspan=2)

        self.lastEntry.grid(row=3, column=3)
        self.firstEntry.grid(row=3, column=1)
        
        self.searchButton.grid(row=3, column=4)
        self.printButton.grid(row=5, column=3)
        
        self.infoLB.grid(row=6,column=0,columnspan=3)

    def getDBinfo(self):
        """open database connection; use cursor to execute select statement to
        retreive all currently forwarding students; store in and return list"""
        
        #Make connection and get a cursor object
        conn = sqlite3.connect('clientDB2.db')
        cursor = conn.cursor()

        #execute SELECT statement
        cursor.execute('''SELECT fname, lname, forwardingAddress, city,
                                        state, zipcode FROM client''')
        #fetch data and store in list        
        all_rows = cursor.fetchall()

        #close connection
        conn.close()
        
        return all_rows

    def fillLB(self, rows):
        """clear and fill listbox with rows from list"""

        #Clear listbox
        self.infoLB.delete(0, 'end')

        #for each row, intsert row into listbox
        for row in rows:
            self.infoLB.insert('end',
                '{1}, {0}: {2}, {3} {4} {5}'.format(row[0], row[1], row[2],
                                                    row[3], row[4], row[5]))

    def search(self):
        """search for names in database; return names if first and/or last
        name match"""

        #retrieve and store all forwarding users in list
        dataRows = self.getDBinfo()

        #retrieve search parameters from entry boxes
        lname = self.lastEntry.get()
        fname = self.firstEntry.get()

        matches = []

        #if search parameters empty display message box; else search list
        if lname == '' and fname == '':
            tkMessageBox.showinfo('Error', 'Please enter first/last name.')
        else:
            for row in dataRows:
                #if first and last name are equal, append to matches
                if fname == row[0] and lname == row[1]:
                    matches.append(row)
                #if only first name is equal, append
                elif fname == row[0]:
                    matches.append(row)
                #if only last name is equal, append
                elif lname == row[1]:
                    matches.append(row)
                    
            #if no matches are appended to list...        
            if matches == []:
                #display message box and refresh listbox
                tkMessageBox.showinfo('No Results', 'No matches found.')
                self.fillLB(dataRows)
            else: #fill list box with matches
                self.fillLB(matches)       
        
    def printLabel(self):
        """print mailing label using user selection from listbox"""

        #get user selection and format for matchObj
        selected = self.infoLB.get('active')
        matchObj = re.match(r'([\w]+), ([\w]+): ([\w\s]+), ([\w\s]+)' ,
                                            selected, re.M|re.I)

        #format string object for printing label
        foo = {'name': matchObj.group(1) + ' ' + matchObj.group(2) ,
               'address': matchObj.group(4), 'state':matchObj.group(3)}

        #store and call labelMaker() from labelCreator
        printLabel = labelCreator.labelMaker(foo)
        printLabel.create_everything()
        
        

def main():
    """the main function"""
    app = Application()
    app.master.title('Mail Center Client GUI')
    app.master.geometry('800x300')
    app.mainloop()

if __name__ == '__main__':
    main()


