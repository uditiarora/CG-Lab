import transform
from graphics import *
import time
def putPixle(win, x, y):
	pt = Point(x,y)	
	pt.draw(win)
        
def drawLine(coords,x1,y1,x2,y2):
	x3,y3 = transform.transformPoint(coords,x1,y1)
	x4,y4 = transform.transformPoint(coords,x2,y2)
	win = GraphWin("Line")
	dx = x4-x3
	dy = y4-y3
	m = 2*dy
	err = m - dx
	y = y1
	for x in range(int(x3),int(x4+1)):
		time.sleep(0.01)
		putPixle(win,x,y)
		err = err + m
		if(err>=0):
			y = y + 1
			err = err - 2 * dx
	
coords = [0,0,500,600,0,0,700,900]
drawLine(coords,90,90,100,100)	

	
	
	

