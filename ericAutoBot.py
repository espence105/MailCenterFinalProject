# Eric Spence
# 11/25/14
# Purpose: Auto-email students who graduated six months ago
import sqlite3 as lite
import datetime
import sys
import smtplib
from email.parser import Parser
import dataBase

MONTHS = ('january', 'february' ,'march', 'april', 'may', 'june','july','august', 'september','october', 'november', 'december')

def get_clients():
    con = lite.connect('clientDB2.db')
    try:
        with con:
            cur = con.cursor()
            #Create the client table if it does not already exist
            cur.execute('''Select * From client WHERE expired is NULL or expired = 0''')
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

    
def check_date(clients):
    nonForward = []
    for client in clients:
        try:
            # foo =  datetime.datetime.strptime(client[8], '%m-%d-%Y')    
            futureDate = client[8].split('-')
            print futureDate
            futureDate[0] = int(futureDate[0])
            print type(futureDate[0])
            futureDate[0] = futureDate[0] + 6
            print futureDate[0]
            if (futureDate[0] > 12):
                futureDate[0] = futureDate[0] - 12 # TODO - make sure this is creating the correct value
                futureDate[2] = int(futureDate[2])+1
            stringFuture = '%d-%d-%d' % (int(futureDate[0]), int(futureDate[1]), int(futureDate[2]))
            future = datetime.datetime.strptime(stringFuture, '%m-%d-%Y')   
            today = datetime.datetime.today()
            print future < today
            if future < today:
                nonForward.append(client)
            
        except:
            print'ERROR', sys.exc_info()[0]
    return nonForward
        # new_row = client[8].split('-')
        # if len(new_row) != 3:
            # new_row = new_row[0].split(' ')

def send_email(expiredClients):
    for client in expiredClients:
        print client[3]
        headers = Parser().parsestr('From: testauemail105@gmail.com\n'
                                     'To: %s\n'
                                     'Subject: Forwarding Expired\n'
                                     '\n'
                                     'Your mail forwarding from Anderson University has expired\n' % ('espence105@gmail.com')) # to send this to other people need to change this to client[3]
        message = 'Subject: Forwarding Expired\n\nYour mail forwarding from Anderson University has expired\n'
        ##### Got help this from stackoverflow ####
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('testaumail105@gmail.com','testpassword105')
        s.sendmail(headers['from'],headers['to'], message)
        s.quit()
        
        #######


def flag_expired(expiredClients):
    for client in expiredClients:
        client = list(client)
        client[9] = 1
        client = tuple(client)
        db = dataBase.DataBase()
        db.update_client_expired((client[9],client[2]))
        

def main():
    clients = get_clients()
    expiredClients = check_date(clients)
    print expiredClients
    send_email(expiredClients)
    flag_expired(expiredClients)

if __name__=='__main__':
    main()
         
        
        
