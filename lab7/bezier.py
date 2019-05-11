from graphics import *
from math import *

def bezier(k,u):
	combi=factorial(n-1)/(factorial(k)*factorial(n-1-k))

	us=0
	if(k==0):
		us=1
	else:
		us=(u**k)

	us1=0
	if(n-1-k==0):
		us1=1
	else:
		us1=(1-u)**(n-1-k)

	temp=combi*us*us1
	return temp

def curve():
	u=0.00
	while(u<=1):
		x=0
		y=0
		z=0
		for k in range(n):
			temp=bezier(k,u)
			x+=(c[k][0]*temp)
			y+=(c[k][1]*temp)

		p=Point(x,y)
		p.draw(win)
		u+=0.01

win = GraphWin('Bezier',600,600)
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
