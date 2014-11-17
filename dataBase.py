# Group Project #
# Purpose: Provide database functionality # 


import sqlite3 as lite
import sys

class DataBase(object):

    
    def __init__(self):
        pass

    def insert_client(self, client_info):
        
        con = lite.connect('clientDB2.db')
        try:
            with con:
                cur = con.cursor()
                cur.executemany("INSERT INTO client VALUES(?,?,?,?,?,?,?,?,?)", (client_info,))
                con.commit
                
        except lite.Error, e:
            if con:
                con.rollback()

            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if con:
                con.close()

        ## IN PROGRESS ##

    """def update_client(self, client_info):

        con = lite.connect('clientDB2.db')
        try:
            with con:
                cur = self.con.cursor()
                cur.execute("SELECT * FROM client")

                rows = cur.fetchall()

                for row in rows:
                    print row
                    
        except lite.Error, e:
            if con:
                con.rollback()

            print "Error %s:"  % e.args[0]
            sys.exit()

        finally:
            if con:
                con.close()"""

    """ def select_client(self, client_info)
        con = lite.connect('clientDB2.db')"""
        
    """def delete_client(self, client_info):
        con = lite.connect('clientDB2.db')
        try:
            with con:
                cur = self.con.cursor()
                cur.execute("DELETE FROM client WHERE fName == 'bob'")

                rows = cur.fetchall()

                for row in rows:
                    print row
                    
        except lite.Error, e:
            if con:
                con.rollback()

            print "Error %s:"  % e.args[0]
            sys.exit()

        finally:
            if con:
                con.close()"""



## FOR TESTING ##
"""def main():
    DB = DataBase()

    client_info = (None, 'bob', 'bob', '1111111', 'bob@bob.bob', 'bob street', 'bobtopia', 'bobland', '00002')

    DB.update_client(client_info)

if __name__ == '__main__':
    main()"""
