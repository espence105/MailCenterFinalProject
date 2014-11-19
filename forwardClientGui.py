#forwardClientGui.py
#November2014
#Jason Samuels
#Students will enter their forwarding information.


import Tkinter as tk # link to the Gui.py file
import tkMessageBox


class ClientFrontend(tk.Frame):
    def __init__(self, master=None):
        
        tk.Frame.__init__(self,master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.introLabel = tk.Label(self, text='Please Enter Forwarding Information')
        self.quitButton = tk.Button(self, text='Save', command = self.login)

        self.userName = tk.Entry(self, width=40)
        self.userName.insert(0,'')

        self.StreetAddressLabel = tk.Label(self, text='Street Address')
        self.StateLabel = tk.Label(self, text='State')
        self.CityLabel = tk.Label(self, text='City')
        self. ZipLabel= tk.Label(self, text='Zip')
        self.EmailLabel = tk.Label(self, text='Email')
       
        
        self.userPassword = tk.Entry(self, width=40, show='')
        self.userPassword.insert(0,'')
        

        
        self.introLabel.grid()
        self.userName.grid(row=1,column=1)
        self.StreetAddressLabel.grid(row=1, column = 0)
        self.StateLabel.grid(row=2,column=0)
        self.CityLabel.grid(row=3, column = 0)
        self.ZipLabel.grid(row=4,column=0)

       
        self.quitButton.grid()

    def login(self):
        if self.attempt_login():
            pass
        else:
            tkMessageBox.showinfo('Incorrect Information', 'Your username or password is incorrect')
        
    def attempt_login(self):
        return False
   
        
        

def main():
    app = ClientFrontend()
    app.master.title('Forwarding Information')
    app.master.geometry("%dx%d%+d%+d" % (500, 150, 400, 400))
    app.mainloop()
    
# Calls the function
if __name__ == '__main__':
    main()

