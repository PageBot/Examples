#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E04_TextA2.py
#
#     Create a page in A2 portrait (as it could be start of a poster)
#     Setup the document view to show registration marks and cropmarks
#     Show the page frame and padding frame in blue
#     Show the generated PDF file name on top of the page.
#     Show red A1 centered on the page as Text element,
#     with its baseline on the middle of page height
#

from pagebot import getContext
from pagebot.constants import *
from pagebot.elements import newText, newRect, newLine
from pagebot.document import Document
from pagebot.toolbox.color import color
from pagebot.toolbox.units import pt, em
from pagebot.toolbox.transformer import path2FileName
H, W = A2 # Standard portrait, swapped to be used as landscape ratio.
padding = pt(40) # Outside measures to accommodate the crop makrs.
sw = pt(0.5) # Stroke width of guide lines
textColor = color(1, 0, 0) # Red of the “A4”
bgColor = color(0.9) # Background color of the text box
FILENAME = path2FileName(__file__)

def makeText(contextName):
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    print('Generating:', exportPath)
    context = getContext(contextName)

    # Make a new document with one text box.
    doc = Document(w=W, h=H, title=exportPath, autoPages=1, context=context)
    view = doc.view # Get the current view of the document.
    view.padding = padding # Make space to show crop marks, etc.
    view.showCropMarks = True
    view.showRegistrationMarks = True
    view.showFrame = True # Show the frame of the  page as blue line
    view.showNameInfo = True # Showing page info and title on top of the page.
    page = doc[1] # Get page on pageNumber, first in row (this is only one now).
    page.padding = padding
    style = dict(font='PageBot-Bold', fontSize=fontSize, tracking=-em(0.02),
            leading=em(1), textFill=textColor, xTextAlign=CENTER)
    bs = context.newString('A2', style)
    print('“A2” text size:', bs.textSize)
    t = newText(bs, parent=page, x=page.w/2, y=page.h/2, fill=bgColor, showOrigin=True,
            xAlign=CENTER, yAlign=MIDDLE_CAP)
    print('Text in box size:', t.w, t.h)

    # Horizontal and vertial lines, to show text center/middle position,
    newLine(parent=page, x=0, y=page.h/2, w=page.w, h=0, stroke=(0, 0, 0.8), strokeWidth=0.5)
    newLine(parent=page, x=page.w/2, y=0, w=0, h=page.h, stroke=(0, 0, 0.8), strokeWidth=0.5)
    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
