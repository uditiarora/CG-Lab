import transform
from graphics import *
import time
from PIL import Image
from IPython.display import display, Image

def drawPolygon(poly,win,color):
	n = len(poly)
	for i in range(n):
		x1,y1,x2,y2 = poly[i]
		l1 = Line(Point(x1,y1),Point(x2,y2))
		l1.setFill(color_rgb(color[0],color[1],color[2]))
		l1.draw(win)
	win.postscript(file="image.eps", colormode='color')
	img = Image.open("image.eps")
	img.save("blank.gif", "gif")
	
def check(color1,color2):
	if(color1[0] == color2[0] and color1[1] == color2[1] and color1[2] == color2[2]):
		return True
	return False
def out_of_range(x1,y1):
	if(x1>=vx2 or x1<=vx1):
		return True	
	if(y1>=vy2 or y1<=vy1):
		return True
	return False
def boundary_util(x1,y1,img,color1,color2):
	#color1 = boundary color color2 = fill color
	if(out_of_range(x1,y1) == True):
		return
	
	if (check(point_color,color1) == False and check(point_color,color2) == False) : 
		pt = Point(x1,y1)	
		pt.draw(win)
		print(x1,y1)
		boundary_util(x1+1,y1,img,color1,color2)
		boundary_util(x1,y1+1,img,color1,color2)
		boundary_util(x1-1,y1,img,color1,color2)
		boundary_util(x1,y1-1,img,color1,color2)
		
def boundary(poly,win,color1,color2):
	x1,y1 = poly[0][0],poly[0][1]
	img = Image(Point(0,0),"blank.gif")
	point_color = img.getPixel(x1,y1)

	cp = img.getAnchor()
	boundary_util(int(cp.getX()),int(cp.getY()),img,color1,color2)



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
"""
coords = [-100,-100,100,100,-100,-100,100,100]
wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
win = GraphWin("boundary",vx2-vx1,vy2-vy1)
win.setCoords(vx1,vy1,vx2,vy2)
x_axis1x,x_axis1y = transform.transformPoint(coords,wx2,0)
x_axis2x,x_axis2y = transform.transformPoint(coords,wx1,0)
y_axis1x,y_axis1y = transform.transformPoint(coords,0,wy2)
y_axis2x,y_axis2y = transform.transformPoint(coords,0,wy1)
x_axis = Line(Point(x_axis1x,x_axis1y),Point(x_axis2x,x_axis2y))
#x_axis.draw(win)
y_axis = Line(Point(y_axis1x,y_axis1y),Point(y_axis2x,y_axis2y))
#y_axis.draw(win)



poly = [[0,5,10,10],[10,10,10,-10],[10,-10,0,-5],[0,-5,-10,-10],[-10,-10,-10,10],[-10,10,0,5]]
color1 = [255,0,255]
color2 = [255,0,0]
drawPolygon(poly,win,color1)

boundary(poly,win,color1,color2)
time.sleep(15)
