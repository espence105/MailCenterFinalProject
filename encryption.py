from passlib.hash import sha256_crypt

def encrypt_password(password):
    hash = sha256_crypt.encrypt(password)
    print hash
    return hash

def check_match(password, hash):
    return sha256_crypt.verify(password, hash)

def main():
    test = encrypt_password('smith')
    print check_match('smth', test)
    
if __name__ == '__main__':
    main()
