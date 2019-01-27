import time
from graphics import *
win = GraphWin("mid point algo line",1000,900)
origin = Point(500,500)
origin.draw(win)
Text(origin,"(0,0)").draw(win)
up = Point(500,150)
down=Point(500,895)
left = Point(50,500)
right = Point(990,500)
up.draw(win)
down.draw(win)
left.draw(win)
right.draw(win)
Text(up,"+y").draw(win)
Text(down,"-y").draw(win)
Text(left,"-x").draw(win)
Text(right,"+x").draw(win)

xaxis = Line(left,right)
yaxis = Line(up,down)
xaxis.draw(win)
yaxis.draw(win)

x0 = int(input("Enter x0 "))
y0 = int(input("Enter y0 "))
x1= int(input("Enter x1 "))
y1 = int(input("Enter y1 "))

m = float((y1-y0)/(x1-x0))
a = (y1-y0)
b = (x0-x1)
xp = x0
yp = y0
if(m<1) :
	d = 2*a + b
	ne = 2*b
	e = 2*a
	for i in range (x0,x1+1):
		pt = Point(500+xp,500-yp)
		pt.draw(win)
		time.sleep(0.5)
		if(d>=0):

			yp = yp+1
			d = d + ne
		d = d+e
		xp = xp+1
#myline = Line(Point(x0,y0),Point(x1,y1))
#myline.draw(win)
