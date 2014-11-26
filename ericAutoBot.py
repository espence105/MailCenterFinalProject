# Eric Spence
# 11/25/14
# Purpose: Auto-email students who graduated six months ago
import sqlite3 as lite
import datetime
import sys\

MONTHS = ('january', 'february' ,'march', 'april', 'may', 'june','july','august', 'september','october', 'november', 'december')

def get_clients():
    con = lite.connect('clientDB2.db')
    try:
        with con:
            cur = con.cursor()
            #Create the client table if it does not already exist
            cur.execute('''Select * From client''')
            all_rows = cur.fetchall()
            return all_rows
    except lite.Error, e:
        #Revert database to previous stable state if insert fails
        if con:
            con.rollback()
        return False
        
            #print "Error %s:" % e.args[0]
            #sys.exit(1)

    finally:
        #Close connection
          if con:
              con.close()

    
def check_date():
    clients = get_clients()
    for client in clients:
        try:
            foo =  datetime.datetime.strptime(client[8], '%m-%d-%Y')
            
            futureDate = client[8].split('-')
            print futureDate
            futureDate[0] = int(futureDate[0])
            print type(futureDate[0])
            futureDate[0] = futureDate[0] + 6
            print futureDate[0]
            if (futureDate[0] > 12):
                futureDate[0] = futureDate[0] - 12 # TODO - make sure this is creating the correct value
                futureDate[2] = int(futureDate[2])+1
            print futureDate
            
        except:
            print'ERROR', sys.exc_info()[0]
        new_row = client[8].split('-')
        if len(new_row) != 3:
             new_row = new_row[0].split(' ')

def main():
    check_date()

if __name__=='__main__':
    main()
         
        
        
