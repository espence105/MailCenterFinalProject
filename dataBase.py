# Group Project #
# Purpose: Provide database functionality # 


import sqlite3 as lite
import sys

class DataBase(object):

    
    def __init__(self):
        self.con = lite.connect('clientDB2.db')

    def insert_client(self, client_info):

        try:
            with self.con:
                cur = self.con.cursor()
                cur.executemany("INSERT INTO client VALUES(?,?,?,?,?,?,?,?,?)", (client_info,))
                self.con.commit
                
        except lite.Error, e:
            if self.con:
                self.con.rollback()

            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if self.con:
                self.con.close()


#def main():
    #DB = DataBase()
    
    #client_info = (None, 'bob', 'bob', '1111111', 'bob@bob.bob', 'bob street', 'bobtopia', 'bobland', '00002')
    #DB.insert_client(client_info)


#if __name__ == '__main__':
    #main()
