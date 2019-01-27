import transform
from graphics import *
import time

def putPixle(win, x, y,coords):
	x1,y1 = transform.transformPoint(coords,x,y)
	pt = Point(x1,y1)	
	pt.draw(win)

def drawP(coords,xc,yc,x,y,win):
	time.sleep(0.5)
	putPixle(win,xc+x, yc+y,coords)
	putPixle(win,xc-x, yc+y,coords)
	putPixle(win,xc+x, yc-y,coords)
	putPixle(win,xc-x, yc-y,coords)
	putPixle(win,xc+y, yc+x,coords)
	putPixle(win,xc-y, yc+x,coords)
	putPixle(win,xc+y, yc-x,coords)
	putPixle(win,xc-y, yc-x,coords) 



def drawCircle(coords,xc,yc,r):
	
	wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
	win = GraphWin("Circle",vx2-vx1,vy2-vy1)
	win.setCoords(vx1,vy1,vx2,vy2)
	x_axis1x,x_axis1y = transform.transformPoint(coords,wx2,0)
	x_axis2x,x_axis2y = transform.transformPoint(coords,wx1,0)
	y_axis1x,y_axis1y = transform.transformPoint(coords,0,wy2)
	y_axis2x,y_axis2y = transform.transformPoint(coords,0,wy1)
	x_axis = Line(Point(x_axis1x,x_axis1y),Point(x_axis2x,x_axis2y))
	x_axis.draw(win)
	y_axis = Line(Point(y_axis1x,y_axis1y),Point(y_axis2x,y_axis2y))
	y_axis.draw(win)
	
	x = 0
	y = r
	d = 3 - 2*r
	drawP(coords,xc,yc,x,y,win)
	while(y>=x):
		x = x+1
		if d>0:
			y = y-1
			d = d + 4*(x-y) + 10
		else:
			d = d + 4*x + 6
		drawP(coords,xc,yc,x,y,win)





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
print("Enter center")
x1 = int(input())
y1 = int(input())
print("enter radius")
r = int(input())
drawCircle(coords,x1,y1,r)



