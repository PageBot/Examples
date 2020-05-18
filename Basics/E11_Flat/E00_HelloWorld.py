# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2017 Thom Janssen <https://github.com/thomgb>
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     E00_HelloWorld.py
#
#	  This examples creates a Hello world" file, by just using
#     Flat functions.
#
import os
from flat import rgb, font, shape, strike, document

fileName = '00_HelloWorld'
if not os.path.exists('_export'):
	os.mkdir('_export')

red = rgb(255, 0, 100)
flatFont = font.open('/Library/Fonts/Georgia Bold.ttf')
figure = shape().stroke(red).width(2.5)
headline = strike(flatFont).color(red).size(20, 24)

d = document(100, 100, 'mm')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(headline.text('Hello world!')).frame(10, 10, 80, 80)
p.image(kind='rgb').png('_export/%s.png' % fileName)
p.svg('_export/%s.svg' % fileName)
d.pdf('_export/%s.pdf' % fileName)