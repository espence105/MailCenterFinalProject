# setup.py
# Eric Spence
# 11/17/14
# Purpose: To install pip and easy_install 
import get_pylabels 
import get_pip
import get_easy_install
import sys

def main():
    # Install Pip #
    try:
        get_pip.main()
    except:
        print 'Already Installed'
    # Install easy install #
    try:
        get_easy_install.main()
    except:
        print 'Already Installed'
    

if __name__=='__main__':
    main()
