from pagebot import getContext

context = getContext()


context.stroke(0, 1)
context.newBezierPath()
context.moveTo((0, 0))
context.lineTo((100, 100))
context.drawPath()

print(context.bezierPath())

# DrawBot Style.

stroke(0)
strokeWidth(1)
p = BezierPath()
print(p)
p.moveTo((200, 0))
p.lineTo((100, 100))
p.closePath()
drawPath(p)
