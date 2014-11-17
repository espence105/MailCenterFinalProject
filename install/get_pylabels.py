from setuptools.command import easy_install

class Pylabels():
    def install_it(self):  
        # Installs Pylabels #
        easy_install.main(["-U", "pylabels"])
        


  
