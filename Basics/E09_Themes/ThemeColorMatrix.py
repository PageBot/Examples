# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#

#     www.pagebot.io
#     Licensed under MIT conditions
#


# -----------------------------------------------------------------------------
#
#     ThemeColorMatrix.py
#
# Import the Theme classes from PageBot.
from pagebot import getContext
from pagebot.themes import ThemeClasses
from pagebot.themes.basetheme import BaseTheme
from pagebot.constants import CENTER # Import some constants that we need.
from pagebot.toolbox.units import upt, pt
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.toolbox.color import color, blackColor

context = getContext('DrawBot')

# Make a new Theme, altering the some slots in the BaseTheme
class FantasyTheme(BaseTheme):
    NAME = 'Fantasy Red'
    BASE_COLORS = dict(
        base2=color(1, 0, 0.2), # Filling 2 base colors as source for range.
        dark3=color(1, 0, 0.5), # Overwriting single slot in the matrix.
        logo=color(spot=300)
    )
# Make another Theme, based on DesignDesign.Space identity colors.
DDS_LOGO = color(spot=165)
class DDSTheme(BaseTheme):
    NAME = 'DesignDesign.Space'
    BASE_COLORS = dict(
        #base1=color('#8080A0'),
        base2=color('#ACACB8'),
        base3=DDS_LOGO,
        logo=DDS_LOGO,
    )

CW = pt(100) # Width of a color cell
CH = CW*1.5 # Height of a color cell
PADDING = pt(60) # Padding between color matrix and page side.
DX = 7 # Number of matrix colums
DY = 7 # Number of matric rows
G = pt(12) # Gutter in point unit between the color cells.

labelFont = findFont('Roboto-Regular') # Find the font in the PageBot resources.
labelSize = pt(16)
labelLeading = pt(18)

# Calculate the page size, based on size of matrix, cells and gutter.
W, H = PADDING*2 + CW*DX + G*(DX-1), PADDING*3 + CH*DY + G*(DY-1)

def drawColor(colorName, x, y, clr):
    # Draw the color cell as square with a value label.
    context.stroke(None)
    context.fill(clr)
    context.rect(x, y+CH-CW, CW, CW)
    context.stroke(blackColor)
    context.strokeWidth(1)
    context.fill(None)
    context.rect(x, y, CW, CH)
    textFill = 0
    labelString = context.newString('%s\n#%s' % (colorName, clr.hex),
        style=dict(font=labelFont, fontSize=labelSize, leading=labelLeading,
        textFill=textFill))
    tw, th = labelString.textSize # Get the size of the label to center it
    context.text(labelString, (x+CW/2-tw/2, y+30)) # Position text in cell

def makeThemePage(themeClass):
    context.newPage(W, H)
    theme = themeClass()
    colorNames = sorted(theme.palette.colorNames)
    cIndex = 0
    context.fill(0)
    titleString = context.newString('PageBot Theme “%s”' % theme.name,
        style=dict(font=labelFont, fontSize=32))
    context.text(titleString, (PADDING, H-2*PADDING*2/3))

    y = 0
    for colorGroup in colorMatrix:
        x = 0
        for colorName in colorGroup:
            try:
                clr = theme.palette[colorName]
                if clr is not None:
                    drawColor(colorName, PADDING + x*(CW+G), H - 2*PADDING - y*(CH+G)-CH, clr)
                cIndex += 1
            except IndexError:
                break
            x += 1
        y += 1

# Define the matrix by theirs palette names.
colorMatrix = (
    ('black', 'gray', 'white', 'background', 'logoLight', 'logo', 'logoDark'),
    ('lightest0', 'lighter0', 'light0', 'base0', 'dark0', 'darker0', 'darkest0'),
    ('lightest1', 'lighter1', 'light1', 'base1', 'dark1', 'darker1', 'darkest1'),
    ('lightest2', 'lighter2', 'light2', 'base2', 'dark2', 'darker2', 'darkest2'),
    ('lightest3', 'lighter3', 'light3', 'base3', 'dark3', 'darker3', 'darkest3'),
    ('lightest4', 'lighter4', 'light4', 'base4', 'dark4', 'darker4', 'darkest4'),
    ('lightest5', 'lighter5', 'light5', 'base5', 'dark5', 'darker5', 'darkest5'),
)
# Make pages for all standard Theme palettes
for themeName, themeClass in ThemeClasses.items():
    makeThemePage(themeClass)
# Add pages for the custom themes that we made.
makeThemePage(FantasyTheme)
makeThemePage(DDSTheme)

# Save the first of the pages in different formats.
# Only the PDF will contain all pages create.
context.saveImage('_export/dds453-theme-color-matrix.pdf')
context.saveImage('_export/dds453-theme-color-matrix.png')
context.saveImage('_export/dds453-theme-color-matrix.svg')
