import time
from graphics import *

def parametric(x1,y1,x2,y2,clipWin):
	xmin,ymin = clipWin[0]
	xmax,ymax = clipWin[1]
	if(x1>=xmin and y1>=ymin and x2<=xmax and y2<=ymax):
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.draw(win)
		return
	tLeft = 0
	tBottom = 0
	tRight = 1
	tTop = 1
	if(x2-x1 != 0):
		tLeft = -(x1-xmin)/(x2-x1)
		tRight = -(x1-xmax)/(x2-x1)
	else:
		y1 = max(y1,ymin)
		y2 = min(y2,ymax)
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.draw(win)
		return
	if(y2-y1 != 0):
		tBottom = -(y1-ymin)/(y2-y1)
		tTop = -(y1-ymax)/(y2-y1)
	else:
		x1 = max(x1,xmin)
		x2 = min(x2,xmax)
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.draw(win)
		return
	tmin = max(0,max(tLeft,tBottom))
	tmax = min(1,min(tRight,tTop))
	x1_new = x1
	y1_new = y1
	x2_new = x2
	y2_new = y2
	print
	if(tmin == tBottom):
		y1_new = ymin
		x1_new = x1 + (x2-x1)*tmin
	if(tmin == tLeft):
		x1_new = xmin
		y1_new = y1 + (y2-y1)*tmin
	if(tmax == tRight):
		x2_new = xmax
		y2_new = y1 + (y2-y1)*tmax
	if(tmax == tTop):
		y2_new = ymax
		x2_new = x1 + (x2-x1)*tmax
	if(x1_new>xmax or y1_new>ymax or x2_new<xmin or y2_new<ymin):
		print("Line outside range")
		return
		
	print("Line from ",x1_new,y1_new,"to",x2_new,y2_new)
	line1 = Line(Point(int(x1_new),int(y1_new)),Point(int(x2_new),int(y2_new)))
	line1.draw(win)

win=GraphWin("Window1",600,600)
win.setCoords(-300,-300,300,300)
xaxis=Line(Point(-300,0),Point(300,0))
yaxis=Line(Point(0,-300),Point(0,300))
xaxis.draw(win)
yaxis.draw(win)

msg = Text(Point(0,0), "(0,0)")
msg.draw(win)

clipWin = [[-100,-100],[100,100]]
xmin,ymin = clipWin[0]
xmax,ymax = clipWin[1]
line1 = Line(Point(xmin,ymin),Point(xmin,ymax))
line1.draw(win)
line1 = Line(Point(xmin,ymin),Point(xmax,ymin))
line1.draw(win)
line1 = Line(Point(xmin,ymax),Point(xmax,ymax))
line1.draw(win)
line1 = Line(Point(xmax,ymax),Point(xmax,ymin))
line1.draw(win)
parametric(-50,-100,100,200,clipWin)
time.sleep(20)




