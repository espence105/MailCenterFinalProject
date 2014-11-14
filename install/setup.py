from setuptools.command import easy_install
import get_pip
import get_easy_install
import cmd

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
    try:
        easy_install.main(["-U", "pylabels"])
    except:
        print 'Already Installed'

    # Install reportlabels #
    easy_install.main(["-U", "reportlab"])



if __name__=='__main__':
    main()
