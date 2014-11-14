import labels
from reportlab.graphics import shapes


specs = labels.Specification(210, 297, 1, 8, 90, 25, corner_radius=2)

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label(label=0, width=0, height=0, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    name = shapes.String(width/2.0, 52, 'Eric Spence', textAnchor="middle")
    label.add(name)
    s = shapes.String(width/2.0, 15, '8888 Taft Hill Court', textAnchor="middle")
    label.add(s)

# Create the sheet.
sheet = labels.Sheet(specs, draw_label, border=True)

# Add a couple of labels.




# Note that any oversize label is automatically trimmed to prevent it messing up
# other labels.
sheet.add_label("Oversized label here")

# Save the file and we are done.
sheet.save('basic.pdf')
