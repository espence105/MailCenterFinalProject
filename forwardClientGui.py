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
        self.saveButton = tk.Button(self, text='Save',command=self.save,width=20)

        self.TypeFirstName = tk.Entry(self, width=40)
        self.TypeFirstName.insert(0,'')
        
        self.TypeLastName = tk.Entry(self, width=40)
        self.TypeLastName.insert(0,'')

        self.TypeStudentID = tk.Entry(self, width=40)
        self.TypeStudentID.insert(0,'')
        
        self.TypeStreetAddress = tk.Entry(self, width=40)
        self.TypeStreetAddress.insert(0,'')

        
        self.TypeState = tk.Entry(self, width=40)
        self.TypeState.insert(0,'')

        self.TypeCity = tk.Entry(self, width=40)
        self.TypeCity.insert(0,'') 

        self.TypeZip = tk.Entry(self, width=40)
        self.TypeZip.insert(0,'')

        self.TypeEmail = tk.Entry(self, width=40)
        self.TypeEmail.insert(0,'')

        
        self.TypeGradDay= tk.Entry(self, width=40)
        self.TypeGradDay.insert(0,'')
       

  

        ##########################################################################
        #Displaying the Textboxes and the labels 
        self.FirstNameLabel = tk.Label(self, text='     First Name:')
        self.LastNameLabel = tk.Label(self, text='Last Name:')
        self.StudentIDLabel = tk.Label(self, text='Student ID:')
        self.StreetAddressLabel = tk.Label(self, text='     Street Address:')
        self.StateLabel = tk.Label(self, text='State:')
        self.CityLabel = tk.Label(self, text='     City:')
        self. ZipLabel= tk.Label(self, text='Zip:')
        self.EmailLabel = tk.Label(self, text='     Email:')
        self.GradDayLabel = tk.Label(self, text='Graduation Year:')

        self.introLabel.grid()
        self.FirstNameLabel.grid(row=2, column =2)
        self.TypeFirstName.grid(row=2,column=3)
        
        self.LastNameLabel.grid(row=2, column = 0,sticky='e')
        self.TypeLastName.grid(row=2,column=1)
        
        self.StudentIDLabel.grid(row=4, column = 0,sticky='e')
        self.TypeStudentID.grid(row=4,column=1)
        
        self.StreetAddressLabel.grid(row=4, column = 2)
        self.TypeStreetAddress.grid(row=4,column=3)
        
        self.StateLabel.grid(row=5,column=0,sticky='e')
        self.TypeState.grid(row=5,column=1)
        
        self.CityLabel.grid(row=5, column = 2)
        self.TypeCity.grid(row=5,column=3)
        
        self.ZipLabel.grid(row=7,column=0,sticky='e')
        self.TypeZip.grid(row=7,column=1)
        
        self.EmailLabel.grid(row=7,column=2)
        self.TypeEmail.grid(row=7,column=3)
        
        self.GradDayLabel.grid(row=9, column = 0,sticky='e')
        self.TypeGradDay.grid(row=9,column=1)

        #Displaying the Textboxes and the labels 
        ###########################################################################
       
        self.saveButton.grid()

        

    def save(self):
        #Setting if variables
        #Validation for inputs
         fname=self.TypeFirstName.get()
         lname=self.TypeLastName.get()
         StudentID=self.TypeStudentID.get()
         Email=self.TypeEmail.get()
         StreetAddress=self.TypeStreetAddress.get()
         City=self.TypeCity.get()
         State=self.TypeState.get()
         Zip=self.TypeZip.get()
         GradDay=self.TypeGradDay.get()
         
            
        
        #If all are not entered at all then disply error message.
        #Validation for inputs

         try:
        
              if len(StudentID) < 7 or len(StudentID)>7:
                  tkMessageBox.showinfo('Error Message','Please enter 7 digit Student ID!  ')

              if len(Zip) < 5 or len(Zip)>5:
                  tkMessageBox.showinfo('Error Message','Please enter 5 digit Zip Code!  ')
                  
              if len(GradDay) < 4 or len(GradDay)>4:
                  tkMessageBox.showinfo('Error Message','Please enter Year of Graduation!  ')
                  
                     
              if fname=='' or lname=='' or StudentID=='' or Email=='' or StreetAddress==''\
              or City==''or State=='' or Zip=='' or GradDay=='':
                  tkMessageBox.showinfo('Error Message','Please enter all info!')
              else:
                  if self.attempt_save():
                      tkMessageBox.showinfo('Updated Info','Info has been Updated and Saved!')
              StudentID=int(self.TypeStudentID.get())
              Zip=int(self.TypeZip.get())
              GradDay=int(self.TypeGradDay.get())
         except ValueError:
                 tkMessageBox.showinfo('Error Message','Please enter correct format for Graduation Date,ZipCode and/or Student ID!  ')
        

        
   
    #attempt save method
    def attempt_save(self):
        '''Connecting to the database and inserting/saving the info
        into the database that the user inputs '''
        
        #Saving data to the database table
        conn = sqlite3.connect('clientDB2.db')
        c = conn.cursor()
        # Insert statement into the table 
        c.execute("INSERT INTO client(fName,lName,studentID,email,forwardingAddress,city,state,zipCode,gradDate) VALUES (?,?,?,?,?,?,?,?,?)",
                   [self.TypeFirstName.get(),self.TypeLastName.get(),self.TypeStudentID.get(),self.TypeEmail.get(),self.TypeStreetAddress.get(),self.TypeCity.get(),self.TypeState.get(),self.TypeZip.get(),self.TypeGradDay.get()])
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

