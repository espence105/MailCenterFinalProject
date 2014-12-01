# labelCreator.py
# Eric Spence
# 11/17/14
# Purpose: to create a label 
import labels
from reportlab.graphics import shapes
import subprocess

# Got parts of this code from pylabels github - basic.py  #
class labelMaker():
    # Constructor 
    def __init__(self, personInfo):
        self.personalInfo = personInfo
        
    # Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 8 rows of
    # labels. Each label is 90mm x 25mm with a 2mm rounded corner. The margins are
    # automatically calculated.
    

    # Create a function to draw each label. This will be given the ReportLab drawing
    # object to draw on, the dimensions (NB. these will be in points, the unit
    # ReportLab uses) of the label, and the object to render.
    def draw_label(self, label, width, height, obj):
        # Just convert the object to a string and print this at the bottom left of
        # the label.
        name = shapes.String(width/2.0, 52, obj['name'], textAnchor="middle")
        label.add(name)
        s = shapes.String(width/2.0, 30, obj['address'], textAnchor="middle")
        label.add(s)
        s = shapes.String(width/2.0, 15, obj['state'], textAnchor="middle")
        label.add(s)
    # draws the label in the pdf file
    def create_everything(self):
        specs = labels.Specification(210, 297, 2, 8, 90, 25, corner_radius=2)
        
        # Create the sheet.
        sheet = labels.Sheet(specs, self.draw_label, border=True)
        # Add a couple of labels.
        sheet.add_label(self.personalInfo)

        # Note that any oversize label is automatically trimmed to prevent it messing up
        # other labels.

        # Save the file and we are done.
        sheet.save('basic.pdf')
        subprocess.Popen('basic.pdf',shell=True)

# main for testing
def main():
    foo = {'name': 'Richard Spence', 'address': '8888 Rochester Hill Court', 'state':'UT'}
    test = labelMaker(foo)
    test.create_everything()

if __name__ == '__main__':
    main()
