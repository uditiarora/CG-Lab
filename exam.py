from graphics import *
from math import *
win = GraphWin("Bezier Curve", 800, 800)
win.setCoords(-400, -400, 400, 400)
xaxis=Line(Point(-400,0),Point(400,0))
xaxis.setArrow("both")
yaxis=Line(Point(0,-400),Point(0,400))
yaxis.setArrow("both")
xaxis.draw(win)
yaxis.draw(win)

def bezier(k,u,n):
	c=factorial(n-1)/(factorial(k)*factorial(n-1-k))
	bez= c * u**k * (1-u)**(n-k-1)
	return bez
	
	
def curve(win,p,n):
	u=0.00
	while(u<=1.00):
		x=0
		y=0
		for k in range(n):
			bez=bezier(k,u,n)
			x+=(p[k][0]*bez)
			y+=(p[k][1]*bez)
		po=Point(x,y)

		po.draw(win)
		u+=0.01
		
print("Enter the 4 control points for curve p:")
lpoint=[]
qcurve = []
for i in range(4):
	lcoord=[]
	x0=int(input("enter the x-coord:"))
	y0=int(input("enter the y-coord:"))
	lcoord.append(x0)
	lcoord.append(y0)
	lpoint.append(lcoord)
for i in range(0,3):
	l=Line(Point(lpoint[i][0],lpoint[i][1]),Point(lpoint[i+1][0],lpoint[i+1][1]))
	l.setFill("blue")
	l.draw(win)
curve(win,lpoint,4)
	
qx0 = lpoint[3][0]
qy0 = lpoint[3][1]
qcurve.append([qx0,qy0])
qx1 = 2*lpoint[3][0] - lpoint[2][0]
qy1 = 2*lpoint[3][1] - lpoint[2][1]
qcurve.append([qx1,qy1])
qx2 = 6*lpoint[3][0] - 8*lpoint[2][0] + 3*lpoint[1][0]
qy2 = 6*lpoint[3][1] - 8*lpoint[2][1] + 3*lpoint[1][1]
qcurve.append([qx2,qy2])

for i in range(0,2):
	l=Line(Point(qcurve[i][0],qcurve[i][1]),Point(qcurve[i+1][0],qcurve[i+1][1]))
	l.setFill("red")
	l.draw(win)
curve(win,qcurve,3)