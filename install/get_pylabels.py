

class Pylabels():
    def install_it(self):
        from setuptools.command import easy_install
        # Installs Pylabels #
        easy_install.main(["-U", "pylabels"])
        


  
