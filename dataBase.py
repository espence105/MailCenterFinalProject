# Group Project #
# Purpose: Provide database functionality # 


import sqlite3 as lite
import sys

class DataBase(object):

    #Initialize the Database Object.  Object has no data members
    def __init__(self):
        pass

    #Insert info into the client table
    def insert_client(self, client_info):
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

            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            #Close connection
            if con:
                con.close()

    

    #Update info in the client table
    def update_client(self, update_info):
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
            if con:
                con.close()

    def select_client(self, client_id):
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
            print "Error %s:" % e.args[0]
            sys.exit()

        finally:
            if con:
                con.close()
        
    def delete_client(self, delete_info):
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

            print "Error %s:"  % e.args[0]
            sys.exit()

        finally:
            if con:
                con.close()



## FOR TESTING ##
    
"""def main():
    DB = DataBase()
    
    client_info = ('bob', 'bob', '1111119', 'bob@bob.bob', 'bob street', 'bobtopia', 'bobland', '00002', '1-1-01')
    id_key = '1111119'
    #DB.insert_client(client_info)
    update_info = ('hank@bill.boomhauer', 'rainey street', 'arlen', 'texas', '33333', '1111116')
    print DB.update_client(update_info)
    print DB.select_client(id_key)

if __name__ == '__main__':
    main()"""
