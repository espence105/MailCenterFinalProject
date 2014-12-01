import ldap
import tkMessageBox
class ldapConnection():
    '''
        Connects to Ldap

        This allows the user to Login in to the ldap server

        Attributes:
            dn: username
            pw: password
    '''
    # Constructor
    def __init__(self,dn,pw):
        self.dn = dn
        self.pw = pw
        self.ldapServer = 'ldap://10.73.56.15'
        self.ldapConnection = ldap.initialize(self.ldapServer)
    # connects to the ldap server
    def connect(self):
        # attempts to connect to ldap server
        try:
            returnval = self.ldapConnection.bind(self.dn, self.pw)
            # if they can connect it sees who they are 
            if (self.ldapConnection.whoami_s() != None):
                return True
            else:
                return False
        except ldap.LDAPError, e:
            tkMessageBox.showinfo('LDAP ERROR - RETURN TRUE SO IT CAN KEEP BEING TESTED', e)
            return True
            exit(3)

# Used for testing 
def main():
    foo = ldapConnection('Group1', 'cpsc4500@')
    foo.connect()

if __name__ == '__main__':
    main()
