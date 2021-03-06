#!/usr/bin/env python3
# encoding: utf-8
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     www.pagebot.io
#     Licensed under MIT conditions
#
# -----------------------------------------------------------------------------
#
#     E08_CJKBabelString.py

from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.constants import *
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color
from pagebot.constants import TOP, CENTER, MIDDLE, LEFT, BASELINE
from pagebot.toolbox.transformer import path2FileName

fontSize = pt(26)
W, H = pt(750, 750)
padding = pt(48)
gutter = pt(18)
FONT_NAME = 'Verdana'
BOLD_NAME = 'Verdana'
FILENAME = path2FileName(__file__)
s = """글자가 일상이 된다 산돌커뮤니케이션 ABCD123 Latin すべての文化集団は，独自の言語，文字，書記システムを持つ．それゆえ，個々の書記システムをサイバースペースに移転することは. ABCD123 Latin"""

def makeText(contextName):
    context = getContext(contextName)
    exportPath = '%s/%s-%s.pdf' % (EXPORT, FILENAME, contextName)
    doc = Document(w=W, h=H, context=context)
    doc.view.showPadding = True

    page = doc[1]
    page.padding = padding

    fsr = context.newString(s, style=dict(font=FONT_NAME, fontSize=fontSize,
            xTextAlign=CENTER))
    fsb = context.newString(s, style=dict(font=BOLD_NAME, fontSize=fontSize,
            xTextAlign=CENTER))
    fsrRed = context.newString(s, style=dict(font=FONT_NAME, textFill=color(1, 0, 0),
        fontSize=fontSize, xTextAlign=CENTER))
    fsrWhite = context.newString(s, style=dict(font=FONT_NAME, textFill=1,
        fontSize=fontSize, xTextAlign=CENTER))

    # All Text elements fit to width of the page, and then float to top,
    # until they hit the bottom margin (e.bm) of the Text element above.
    conditions = [Fit2Width(), Float2Top()]

    newText(fsr, conditions=conditions, parent=page, mb=gutter)
    newText(fsb, conditions=conditions, parent=page, mb=gutter)
    # Text in red
    newText(fsrRed, conditions=conditions, parent=page, mb=gutter/2)
    # Text is white on black background
    newText(fsrWhite, conditions=conditions, parent=page, padding=pt(20, 40, 10, 40),
            textFill=1, fill=0.2, mb=2.5*gutter, showPadding=True)
    # Text is white on red background
    newText(fsrWhite, conditions=conditions, parent=page, xTextAlign=LEFT, yAlign=BASELINE,
            padding=pt(20), showMargin=True, showPadding=True,
            textFill=1, fill=(1, 0, 0))

    doc.solve()

    doc.export(exportPath)

for contextName in ('DrawBot', 'Flat'):
    makeText(contextName)
