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
    # Installs Pylabels #
    foo = get_pylabels.Pylabels()
    foo.install_it()
    

if __name__=='__main__':
    main()
