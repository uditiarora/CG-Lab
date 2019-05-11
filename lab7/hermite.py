from graphics import *
from math import *

def hermite(u):
	h0=2*u**3-3*u**2+1
	h1=-2*u**3+3*u**2
	h2=u**3-2*u**2+u
	h3=u**3-u**2
	h=[h0,h1,h2,h3]
	return h

def curve():
	u=0.00
	while(u<=1):
		x=0
		y=0
		z=0
		h=hermite(u)
		x=c[0][0]*h[0] + c[1][0]*h[1] + c[0][0]*1*h[2] + c[1][0]*1*h[3]
		y=c[0][1]*h[0] + c[1][1]*h[1] + c[0][1]*-1*h[2] + c[1][1]*1*h[3]
		p=Point(x,y)
		p.draw(win)
		u+=0.01

win = GraphWin('Hermite',600,600)
win.setCoords(-300,-300,300,300)
l = Line(Point(-300,0),Point(300,0))
l.draw(win)
l1 = Line(Point(0,300),Point(0,-300))
l1.draw(win)

n=int(input("Enter number of control points : "))

c=[]
temp=[]
for i in range(n):
	temp=[]
	print("\n\nNew sides")
	x = int(input("Enter new x = "))
	y = int(input("Enter new y = "))
	temp.append(x)
	temp.append(y)
	p=Point(x,y)
	p.draw(win)
	c.append(temp)

curve()

win.getMouse();
win.close();
