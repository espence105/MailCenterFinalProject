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

    # Install reportlabels - dont think that this will work will test on a lab computer #
    try:
        easy_install.main(["-U", "reportlab"])
    except:
        print 'Already Installed'


if __name__=='__main__':
    main()
