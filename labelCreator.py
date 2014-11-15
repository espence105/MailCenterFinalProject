
import labels
from reportlab.graphics import shapes

# Got this code from pylabels github - with  #
class labelMaker():
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
        s = shapes.String(width/2.0, 15, obj['address'], textAnchor="middle")
        label.add(s)

    def create_everything(self):
        specs = labels.Specification(210, 297, 2, 8, 90, 25, corner_radius=2)
        
        # Create the sheet.
        sheet = labels.Sheet(specs, self.draw_label, border=True)
        foo = {'name': 'Eric Spence', 'address': '8888 Taft Hill Court'}
        # Add a couple of labels.
        sheet.add_label(self.personalInfo)


        # We can also add each item from an iterable.


        # Note that any oversize label is automatically trimmed to prevent it messing up
        # other labels.

        # Save the file and we are done.
        sheet.save('basic.pdf')
        print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))

def main():
    foo = {'name': 'Eric Spence', 'address': '8888 Taft Hill Court'}
    test = labelMaker(foo)
    test.create_everything()
