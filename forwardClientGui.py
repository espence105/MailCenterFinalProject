#forwardClientGui.py
#November2014
#Jason Samuels
#Students will enter their forwarding information.

#Using Tkinter
import Tkinter as tk # link to the Gui.py file
import tkMessageBox
#Connecting to the database
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

        self.TypeFirstName = tk.Entry(self, width=40)
        self.TypeFirstName.insert(0,'Jason')
        
        self.TypeLastName = tk.Entry(self, width=40)
        self.TypeLastName.insert(0,'Samuels')

        self.TypeStudentID = tk.Entry(self, width=40)
        self.TypeStudentID.insert(0,'2081362')
        
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

        self.TypeGradDay= tk.Entry(self, width=40)
        self.TypeGradDay.insert(0,'May 2015')

  

        ##########################################################################
        #Displaying the Textboxes and the labels 
        self.FirstNameLabel = tk.Label(self, text='First Name:')
        self.LastNameLabel = tk.Label(self, text='Last Name:')
        self.StudentIDLabel = tk.Label(self, text='Student ID:')
        self.StreetAddressLabel = tk.Label(self, text='Street Address:')
        self.StateLabel = tk.Label(self, text='State:')
        self.CityLabel = tk.Label(self, text='City:')
        self. ZipLabel= tk.Label(self, text='Zip:')
        self.EmailLabel = tk.Label(self, text='Email:')
        self.GradDayLabel = tk.Label(self, text='Graduation Date:')
       
        

        

        
        self.introLabel.grid()
        self.TypeFirstName.grid(row=1,column=1)
        self.TypeLastName.grid(row=2,column=1)
        self.TypeStudentID.grid(row=3,column=1)
        self.TypeStreetAddress.grid(row=4,column=1)
        self.TypeState.grid(row=5,column=1)
        self.TypeCity.grid(row=6,column=1)
        self.TypeZip.grid(row=7,column=1)
        self.TypeEmail.grid(row=8,column=1)
        self.TypeGradDay.grid(row=9,column=1)
       

        self.FirstNameLabel.grid(row=1, column = 0)
        self.LastNameLabel.grid(row=2, column = 0)
        self.StudentIDLabel.grid(row=3, column = 0)
        self.StreetAddressLabel.grid(row=4, column = 0)
        self.StateLabel.grid(row=5,column=0)
        self.CityLabel.grid(row=6, column = 0)
        self.ZipLabel.grid(row=7,column=0)
        self.EmailLabel.grid(row=8,column=0)
        self.GradDayLabel.grid(row=9, column = 0)
        #Displaying the Textboxes and the labels 
        ###########################################################################
       
        self.saveButton.grid()

    def save(self):
        if self.attempt_save():
            tkMessageBox.showinfo('Updated Info','Info has been Updated and Saved')

    def attempt_save(self):
        #Saving data to the database table
         conn = sqlite3.connect('clientDB2.db')
         c = conn.cursor()
        # Insert statement into the table 
         c.execute("INSERT INTO client(fName,lName,studentID,email,forwardingAddress,city,state,zipCode,gradDate) VALUES (?,?,?,?,?,?,?,?,?)",[self.TypeFirstName.get(),self.TypeLastName.get(),self.TypeStudentID.get(),self.TypeEmail.get(),self.TypeStreetAddress.get(),self.TypeCity.get(),self.TypeState.get(),self.TypeZip.get(),self.TypeGradDay.get()])
         conn.commit()

         c.close()
         conn.close()
         
         #Deleting all of the Entries after saving data
         self.TypeFirstName.delete(0,tk.END)
         self.TypeLastName.delete(0,tk.END)
         self.TypeStudentID.delete(0,tk.END)
         self.TypeStreetAddress.delete(0,tk.END)
         self.TypeState.delete(0,tk.END)
         self.TypeCity.delete(0,tk.END)
         self.TypeZip.delete(0,tk.END)
         self.TypeEmail.delete(0,tk.END)
         self.TypeGradDay.delete(0,tk.END)

         
         print ("Saved")
         return True

        
        
   
        
        
#The main function 
def main():
    app = ClientFrontend()
    app.master.title('Forwarding Information')
    app.master.geometry("%dx%d%+d%+d" % (1000, 370, 300, 300))
    app.mainloop()
    
# Calls the function
if __name__ == '__main__':
    main()

