#forwardClientGui.py
#November2014
#Jason Samuels
#Students will enter their forwarding information.

#Using Tkinter
import Tkinter as tk # link to the Gui.py file
import tkMessageBox
import sqlite3
conn = sqlite3.connect('clientDB2.db')


class ClientFrontend(tk.Frame):
    def __init__(self, master=None):
        
        tk.Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        

#These are the widgets.
    def create_widgets(self):
        self.introLabel = tk.Label(self, text='Please Enter Forwarding Information (All Is Required)')
        self.saveButton = tk.Button(self, text='Save',command=self.save)
        
        self.TypeStreetAddress = tk.Entry(self, width=40)
        self.TypeStreetAddress.insert(0,'5555 Candy Apple Lane')
        
        self.TypeState = tk.Entry(self, width=40)
        self.TypeState.insert(0,'Indiana')

        self.TypeCity = tk.Entry(self, width=40)
        self.TypeCity.insert(0,'Indianapolis')

        self.TypeZip = tk.Entry(self, width=40)
        self.TypeZip.insert(0,'46226')

        self.TypeEmail = tk.Entry(self, width=40)
        self.TypeEmail.insert(0,'hello@anderson.edu')

  

        ##########################################################################
        #Displaying the Textboxes
        self.StreetAddressLabel = tk.Label(self, text='Street Address:')
        self.StateLabel = tk.Label(self, text='State:')
        self.CityLabel = tk.Label(self, text='City:')
        self. ZipLabel= tk.Label(self, text='Zip:')
        self.EmailLabel = tk.Label(self, text='Email:')
       
        

        

        
        self.introLabel.grid()
        self.TypeStreetAddress.grid(row=1,column=1)
        self.TypeState.grid(row=2,column=1)
        self.TypeCity.grid(row=3,column=1)
        self.TypeZip.grid(row=4,column=1)
        self.TypeEmail.grid(row=5,column=1)
        #Displaying the Textboxes
        ###########################################################################

        
        self.StreetAddressLabel.grid(row=1, column = 0)
        self.StateLabel.grid(row=2,column=0)
        self.CityLabel.grid(row=3, column = 0)
        self.ZipLabel.grid(row=4,column=0)
        self.EmailLabel.grid(row=5,column=0)

       
        self.saveButton.grid()

    def save(self):
        if self.attempt_save():
            tkMessageBox.showinfo('Info has been Updated and Saved')
        
    def attempt_save(self):
         conn = sqlite3.connect('clientDB2.db')
         c = conn.cursor()
         c.execute('PRAGMA foreign_keys = ON')
         conn.commit()

         customerData = [(None, self.TypeStreetAddress, self.TypeState, self.TypeCity, self.TypeZip, self.TypeEmail)]

         for element in customerData:
             c.executemany("INSERT INTO Client VALUES (?,?,?,?,?,?,?,?,?)", (element,))
         conn.commit()

         c.close()
         conn.close()

         self.TypeStreetAddress.delete(0, END)
         self.TypeState.delete(0, END)
         self.TypeCity.delete(0, END)
         self.TypeZip.delete(0, END)
         self.TypeEmail.delete(0, END)
         

         print ("Saved")
         return True
        
   
        
        

def main():
    app = ClientFrontend()
    app.master.title('Forwarding Information')
    app.master.geometry("%dx%d%+d%+d" % (1000, 170, 300, 300))
    app.mainloop()
    
# Calls the function
if __name__ == '__main__':
    main()

