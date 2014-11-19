from subprocess import check_output

class Pylabels():
    """
        Installs Pylabels and reportlab

        This class uses easy tools and pip to install pylabels and reportlab
        which are both modules used in creating the labels

        Attributes:
        none
    """
    # installs the modules
    def install_it(self):
        # has to be imported here because it is installed earlier in the installation proccess
        from setuptools.command import easy_install
        # Installs Pylabels #
        easy_install.main(["-U", "pylabels"])
        # Installs reportlab
        check_output('python -m pip install -U reportlab', shell = True)

# used to call the install function
def main():
    new = Pylabels() 
    new.install_it()
        
if __name__ == '__main__':
    main()

  
