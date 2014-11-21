# Group Project #
# Purpose: Provide database functionality # 


import sqlite3 as lite
import sys

class DataBase(object):

    #Initialize the Database Object.  Object has no data members
    def __init__(self):
        pass

    
    def insert_client(self, client_info):
        """ Inserts a new row into the client table. Method is passed a tuple that
            contains necessary information for database.  Uses SQLite statement
            to insert data.  Will revert database to pre-query state if insert
            fails. """
        #Connect to database.  Will also create new database if it does not exist.
        con = lite.connect('clientDB2.db')
        try:
            with con:
                cur = con.cursor()
                #Create the client table if it does not already exist
                cur.execute('CREATE TABLE IF NOT EXISTS client(fName TEXT NOT NULL, lName TEXT NOT NULL, studentID TEXT NOT NULL, email TEXT NOT NULL, forwardingAddress TEXT NOT NULL, city TEXT NOT NULL, state TEXT NOT NULL, zipCode TEXT NOT NULL, gradDate TEXT NOT NULL)')

                cur.executemany('INSERT INTO client VALUES(?,?,?,?,?,?,?,?,?)', (client_info,))
                con.commit
                
        except lite.Error, e:
            #Revert database to previous stable state if insert fails
            if con:
                con.rollback()

            #print "Error %s:" % e.args[0]
            #sys.exit(1)

        finally:
            #Close connection
            if con:
                con.close()

    

    def update_client(self, update_info):
        """ Attempts to update client info.  Method is passed a tuple containing
            updatable information (email, address, city, state, zip code), as
            well as the student ID to find the user in the database.  Reverts
            database to pre-update state if query fails. """
        
        #Connect to database.  Will also create new database if it does not exist.
        con = lite.connect('clientDB2.db')
        try:
            with con:
                cur = con.cursor()
                #Create the client table if it does not already exist
                cur.execute('CREATE TABLE IF NOT EXISTS client(fName TEXT NOT NULL, lName TEXT NOT NULL, studentID TEXT NOT NULL, email TEXT NOT NULL, forwardingAddress TEXT NOT NULL, city TEXT NOT NULL, state TEXT NOT NULL, zipCode TEXT NOT NULL, gradDate TEXT NOT NULL)')
                
                cur.executemany('UPDATE client SET email=?, forwardingAddress=?, city=?, state=?, zipCode=? WHERE studentID = ?', (update_info,))

                cur.execute('SELECT * FROM client WHERE studentID = ?', (update_info[5],))
                row = cur.fetchall()
                return row
                    
        except lite.Error, e:
            if con:
                con.rollback()
            
            #print "Error %s:"  % e.args[0]
            #sys.exit()

        finally:
            #Close connection
            if con:
                con.close()

    def select_client(self, client_id):

        """ Attempts to pull client info from the database.  Method is passed the
            user's student ID and pulls their info with a SEELCT statement. """
        
        #Connect to database.  Also creates a new database if it does not exist.
        con = lite.connect('clientDB2.db')

        try:
            with con:
                cur = con.cursor()
                #Create the client table if it does not already exist
                cur.execute('CREATE TABLE IF NOT EXISTS client(fName TEXT NOT NULL, lName TEXT NOT NULL, studentID TEXT NOT NULL, email TEXT NOT NULL, forwardingAddress TEXT NOT NULL, city TEXT NOT NULL, state TEXT NOT NULL, zipCode TEXT NOT NULL, gradDate TEXT NOT NULL)')

                cur.execute('SELECT * FROM client WHERE studentID = ?', (client_id,))

                row = cur.fetchall()
                return row
        except lite.Error, e:
            if con:
                con.rollback()
            #print "Error %s:" % e.args[0]
            #sys.exit()

        finally:
            #Close connection
            if con:
                con.close()
        
    def delete_client(self, delete_info):

        """ Attempts to delete a row from the client table.  Takes user's student
            ID and removes the associated row.  Reverts database to pre-query state
            if delete fails.  To be used only by mail center. """
        
        #Connects to database.  Creates a new one if it does not exist.
        con = lite.connect('clientDB2.db')
        try:
            with con:
                
                #Create the client table if it does not already exist
                cur.execute('CREATE TABLE IF NOT EXISTS client(fName TEXT NOT NULL, lName TEXT NOT NULL, studentID TEXT NOT NULL, email TEXT NOT NULL, forwardingAddress TEXT NOT NULL, city TEXT NOT NULL, state TEXT NOT NULL, zipCode TEXT NOT NULL, gradDate TEXT NOT NULL)')

                
                cur = self.con.cursor()
                cur.execute('DELETE FROM client WHERE studentID == ?', (delete_info,))
                
                    
        except lite.Error, e:
            if con:
                con.rollback()

            #print "Error %s:"  % e.args[0]
            #sys.exit()

        finally:
            #Close connection
            if con:
                con.close()


    def insert_employee(self, employee_username):
        """ Allows a new employee to be added to the database for verification
            purposes.  Attempts to insert username of employee.  Reverts database
            to pre-query state if insert fails. Only to be used by mail center"""

        #Connect to database.  Creates a new one if it does not exits.
        con = lite.connect('clientDB2.db')
        try:
            with con:

                #Create the employee table if it does not exist
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS employee(username TEXT NOT NULL)')

                
                cur.execute('INSERT INTO employee VALUES (?)', (employee_username,))

        except lite.Error, e:
            if con:
                con.rollback()

            #print "Error %s:" %e.args[0]
            #sys.exit()
                
        finally:
            #Close connection
            if con:
                con.close()

    def select_employee(self, employee_username):
        """ Attempts to pull the username from the database.  If successful,
            the user is a mail center employee """
        #Connect to database.  Creates new one if it does not exist.
        con = lite.connect('clientDB2.db')

        try:
            with con:
                #Creates the employee table if it does not exist
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS employee(username TEXT NOT NULL)')

                
                cur.execute('SELECT * FROM employee WHERE username = ?', (employee_username,))

                row = cur.fetchone()

                if row == None:
                    return False
                else:
                    return True
        except lite.Error, e:
            if con:
                con.rollback()

            #print "Error %s:" %e.args[0]
            #sys.exit()
                
        finally:
            #Close connection
            if con:
                con.close()

    def insert_nonstudent(self, nonstudent_info):
        """ Attempts to insert information for clients that are not AU students.
            Rolls back the database to last stable instance if fails.  Only
            to be used by mail center employees. """

        #Connect to database.  Create a new one if it does not exist.
        con = lite.connect('clientDB2.db')

        try:
            with con:
                #Create the nonstudent table if it does not exist
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS nonstudent(username TEXT NOT NULL, password TEXT NOT NULL, fName TEXT NOT NULL, lName TEXT NOT NULL)')

                cur.execute('INSERT INTO nonstudent VALUES(?,?,?,?)', (nonstudent_info,))
        except lite.Error, e:
            if con:
                con.rollback()
            #print "Error %s:" %e.args[0]
            #sys.exit()
        finally:
            if con:
                con.close()

    def insert_nonstudent(self, nonstudent_username):
        """ Attempts to insert information for clients that are not AU students.
            Rolls back the database to last stable instance if fails.  Only
            to be used by mail center employees. """

        #Connect to database.  Create a new one if it does not exist.
        con = lite.connect('clientDB2.db')

        try:
            with con:
                #Create the nonstudent table if it does not exist
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS nonstudent(username TEXT NOT NULL, password TEXT NOT NULL, fName TEXT NOT NULL, lName TEXT NOT NULL)')

                cur.execute('DELETE FROM nonstudent WHERE username = ?', (nonstudent_username,))
        except lite.Error, e:
            if con:
                con.rollback()
            #print "Error %s:" %e.args[0]
            #sys.exit()
        finally:
            if con:
                con.close()

    


## FOR TESTING ##
def main():
    DB = DataBase()
    DB.insert_employee('Group1')
    

if __name__ == '__main__':
    main()
