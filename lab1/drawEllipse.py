import transform
from graphics import *
import time
def putPixle(win, x, y,coords):
	time.sleep(0.1)
	x1,y1 = transform.transformPoint(coords,x,y)
	pt = Point(x1,y1)	
	pt.draw(win)


def drawEllipse(coords,xc,yc,rx,ry):
	wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
	win = GraphWin("Ellipse",vx2-vx1,vy2-vy1)
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
	y = ry
	p = (ry*ry) - (rx*rx*ry) + ((rx*rx)/4)
	while((2*x*ry*ry) < (2*y*rx*rx)):
		putPixle(win,xc+x,yc-y,coords)
		putPixle(win,xc-x,yc+y,coords)
		putPixle(win,xc+x,yc+y,coords)
		putPixle(win,xc-x,yc-y,coords)
		if(p<0):
			x = x+1
			p = p + (2*ry*ry*x) + (ry*ry)
		else:
			x = x+1
			y = y-1
			p = p + (2*ry*ry*x + ry*ry) - (2*rx*rx*y)
	p = (float(x) + 0.5)*(float(x)+0.5)*ry*ry + (y-1)*(y-1)*rx*rx - rx*rx*ry*ry
	while(y>=0):
		putPixle(win,xc+x,yc-y,coords)
		putPixle(win,xc-x,yc+y,coords)
		putPixle(win,xc+x,yc+y,coords)
		putPixle(win,xc-x,yc-y,coords)
		if(p>0):
			y = y-1
			p = p - (2*rx*rx*y) + (rx*rx)
		else:
			y = y-1
			x = x+1
			p = p + (2*ry*ry*x) - (2*rx*rx*y) - (rx*rx)

 
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
print("Enter radius 1 and 2")
a = int(input())
b = int(input())
drawEllipse(coords,x1,y1,a,b)
