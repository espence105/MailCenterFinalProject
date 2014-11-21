import ldap

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
            print 'connected'
            # if they can connect it sees who they are 
            if (self.ldapConnection.whoami_s() != None):
                print self.ldapConnection.whoami_s()
                print 'Autenticated!'
            else:
                print 'Invalid login'
        except ldap.LDAPError, e:
            print 'Error: ', e
            exit(3)

# Used for testing 
def main():
    foo = ldapConnection('Group1asdf', 'cpsc4500@')
    foo.connect()

if __name__ == '__main__':
    main()
