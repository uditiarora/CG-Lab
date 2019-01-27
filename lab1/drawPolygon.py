import transform
from graphics import *
def putPixle(win, x, y):
	time.sleep(0.1)
	x1,y1 = transform.transformPoint(coords,x,y)
	pt = Point(x1,y1)	
	pt.draw(win)
	
def swap(x,y):
	return y,x
def drawLine(win,coords,x0,y0,x1,y1):
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	slope = 0
	if(dx==0):
		x2,y2 = transform.transformPoint(coords,x0,y0)
		x3,y3 = transform.transformPoint(coords,x1,y1)
		l1 = Line(Point(x2,y2),Point(x3,y3))
		l1.setWidth(2)
		l1.draw(win)
		time.sleep(2.5)
		return
	else:	
		slope = dy/float(dx)
	x, y = x0, y0
	if slope > 1:
	    dx, dy = dy, dx
	    x, y = y, x
	    x0, y0 = y0, x0
	    x1, y1 = y1, x1
	p = 2 * (dy - dx)
	putPixle(win, x, y)
	for k in range(2, dx+1):
	    if p > 0:
	        y = y + 1 if y < y1 else y - 1
	        p = p + 2*(dy - dx)
	    else:
	        p = p + 2*dy
	    x = x + 1 if x < x1 else x - 1
	    putPixle(win, x, y)	
					
		

def drawPolygon(coords,points):
	#points is a 2d array. each row contains (x1,y1),(x2,y2) which signifies 1 line of the polygon
	wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
	win = GraphWin("Line",vx2-vx1,vy2-vy1)
	win.setCoords(vx1,vy1,vx2,vy2)
	x_axis1x,x_axis1y = transform.transformPoint(coords,wx2,0)
	x_axis2x,x_axis2y = transform.transformPoint(coords,wx1,0)
	y_axis1x,y_axis1y = transform.transformPoint(coords,0,wy2)
	y_axis2x,y_axis2y = transform.transformPoint(coords,0,wy1)
	x_axis = Line(Point(x_axis1x,x_axis1y),Point(x_axis2x,x_axis2y))
	x_axis.draw(win)
	y_axis = Line(Point(y_axis1x,y_axis1y),Point(y_axis2x,y_axis2y))
	y_axis.draw(win)
	
	for i in range(0,len(points)):
		x1,y1,x2,y2 = points[i]
		drawLine(win,coords,x1,y1,x2,y2)

	
	
"""
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
print("Enter number of egdes of polygon")
n = int(input())
points = []
for i in range(n):
	print("Enter points connecting lines of polygon")
	x1 = int(input())
	y1 = int(input())
	x2 = int(input())
	y2 = int(input())	
	points.append([x1,y1,x2,y2])
drawPolygon(coords,points)
	"""
coords = [-100,-100,100,100,-100,-100,100,100]
points = [[0,50,25,25],[25,25,25,-25],[25,-25,0,-50],[0,-50,-25,-25],[-25,-25,-25,25],[-25,25,0,50]]
drawPolygon(coords,points)



