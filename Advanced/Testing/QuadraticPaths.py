#!/usr/bin/env python3
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     BezierPaths.py
#

from pagebot.constants import A4Rounded
from drawBot import BezierPath as DrawBotBezierPath
from pagebot.contexts.basecontext.basebezierpath import BaseBezierPath
from pagebot.contexts.basecontext.bezierpath import BezierPath
from pagebot import getAllContexts
from pagebot.toolbox.units import pt

H, W = A4Rounded
W = pt(W)
H = pt(H)

def testBezierPath(path):
    # Replicates FontTools BasePen test.

    path.moveTo((0, 0))
    path.lineTo((0, 100))
    path.curveTo((50, 75), (60, 50), (50, 25))
    #path.curveTo((50, 75), (60, 50), (50, 25), (0, 0))
    path.closePath()

def printBezierPath(path):

    for contour in path.contours:
        for i, segment in enumerate(contour):
            print("#%s: %s" % (i, segment))

    print(path.points)

def testBezierPaths():
    path = DrawBotBezierPath()
    testBezierPath(path)
    nsPath = path._path

    print("NSPath")
    print(nsPath)
    count = nsPath.elementCount()
    points = []

    for index in range(nsPath.elementCount()):
        instruction, pts = nsPath.elementAtIndex_associatedPoints_(index)
        points.extend([(p.x, p.y) for p in pts])

    points = tuple(points)
    print(points)

    print("DrawBot: <BezierPath>")
    printBezierPath(path)

    '''
    # TODO:
    # testing the "no on-curve point" scenario
    pen.qCurveTo((0, 0), (0, 100), (100, 100), (100, 0), None)
    pen.closePath()
    '''
    print("PageBot:")

    contexts = getAllContexts()

    for i, c in enumerate(contexts):
        if i in (0, 1):
            path = c.newPath()
            print(path)
            testBezierPath(path)
            printBezierPath(path)

testBezierPaths()
