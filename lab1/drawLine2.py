import transform
from graphics import *
import time
def putPixle(win, x, y):
	time.sleep(0.1)
	x1,y1 = transform.transformPoint(coords,x,y)
	pt = Point(x1,y1)	
	pt.draw(win)
	
def swap(x,y):
	return y,x
def drawLine(coords,x0,y0,x1,y1):
	
			wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
			win = GraphWin("Line",vx2-vx1,vy2-vy1)
			x_axis1x,x_axis1y = transform.transformPoint(coords,wx2,0)
			x_axis2x,x_axis2y = transform.transformPoint(coords,wx1,0)
			y_axis1x,y_axis1y = transform.transformPoint(coords,0,wy2)
			y_axis2x,y_axis2y = transform.transformPoint(coords,0,wy1)
			x_axis = Line(Point(x_axis1x,x_axis1y),Point(x_axis2x,x_axis2y))
			x_axis.draw(win)
			y_axis = Line(Point(y_axis1x,y_axis1y),Point(y_axis2x,y_axis2y))
			y_axis.draw(win)
			dx = abs(x1 - x0)
			dy = abs(y1 - y0)
			slope = dy/float(dx)
			x, y = x0, y0
			if slope > 1:
			    dx, dy = dy, dx
			    x, y = y, x
			    x0, y0 = y0, x0
			    x1, y1 = y1, x1
			p = 2 * (dy - dx)
			putPixle(win, x, y)
			for k in range(2, dx):
			    if p > 0:
			        y = y + 1 if y < y2 else y - 1
			        p = p + 2*(dy - dx)
			    else:
			        p = p + 2*dy
			    x = x + 1 if x < x1 else x - 1
			    putPixle(win, x, y)			
		
		
		
print("Enter minimum co-ordinates of window")
wx1 = int(input())
wy1 = int(input())
print("Enter maximum co-ordinates of window")
wx2 = int(input())
wy2 = int(input())
print("Enter minimum co-ordinates of viewport")
vx1 = int(input())
vy1 = int(input())
print("Enter maximum co-ordinates of viewport")
vx2 = int(input())
vy2 = int(input())
coords = [wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2]
print("Enter points")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
drawLine(coords,x1,y1,x2,y2)





