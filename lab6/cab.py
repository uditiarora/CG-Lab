#cabinet projection
from graphics import *
from math import *
def setWindow(win):
	win.setCoords(-400, -400, 400, 400)
	xaxis=Line(Point(-400,0),Point(400,0))
	xaxis.setArrow("both")
	yaxis=Line(Point(0,-400),Point(0,400))
	yaxis.setArrow("both")
	zaxis=Line(Point(200,200),Point(-200,-200)) 
	zaxis.setArrow("both")
	xaxis.draw(win)
	yaxis.draw(win)
	zaxis.draw(win)

def drawLine(x0,y0,z0,x1,y1,z1,color,win): 
	xnew1=x0-(z0*0.3)
	ynew1=y0-(z0*0.3)
	xnew2= x1-(z1*0.3)
	ynew2= y1-(z1*0.3)
	line=Line(Point(xnew1,ynew1),Point(xnew2,ynew2));
	line.setFill(color)
	line.draw(win)
	
def draw3dobj(vertex1,vertex2,clr,n,win):
    for i in range(n):
    	x0 = vertex1[i][0]
    	y0 = vertex1[i][1]
    	z0 = vertex1[i][2]
    	x1 = vertex2[i][0]
    	y1 = vertex2[i][1]
    	z1 = vertex2[i][2]
    	drawLine(x0,y0,z0,x1,y1,z1,clr,win)

def main():
	win = GraphWin("cabinet projection", 800, 800)
	setWindow(win)
	color1="red"
	color2="blue"
	f=open("input.txt","r")
	n=int(f.readline())
	vertex1=[]
	vertex2=[]
	for i in range(n):
		a=f.readline().strip()
		l=a.split(' ')
		narr=[]
		for i in l:
			narr.append(int(i))
		lpoint=[]
		lpoint.append(narr[0])
		lpoint.append(narr[1])
		lpoint.append(narr[2])
		vertex1.append(lpoint)
		lpoint=[]
		lpoint.append(narr[3])
		lpoint.append(narr[4])
		lpoint.append(narr[5])
		vertex2.append(lpoint)
	draw3dobj(vertex1,vertex2,color1,n,win)
	matxy=[[1,0,0],[0,1,0],[0.5*cos(radians(63.4)),0.5*sin(radians(63.4)),0]]
	matyz=[[0,1,0],[0,0,1],[0,0.5*cos(radians(63.4)),0.5*sin(radians(63.4))]]
	matxz=[[0,0,1],[1,0,0],[0.5*cos(radians(63.4)),0,0.5*sin(radians(63.4))]]
	choice=int(input("Enter the plane:\n XY plane=1\nYZ plane=2\nXZ plane=3:"))
	if(choice==1):
		for i in range(n):
			vertex1[i][0]=vertex1[i][0]*matxy[0][0]+vertex1[i][1]*matxy[1][0]+vertex1[i][2]*matxy[2][0]
			vertex1[i][1]=vertex1[i][1]*matxy[0][1]+vertex1[i][1]*matxy[1][1]+vertex1[i][2]*matxy[2][1]
			vertex1[i][2]=vertex1[i][0]*matxy[0][2]+vertex1[i][1]*matxy[1][2]+vertex1[i][2]*matxy[2][2]
			vertex2[i][0]=vertex2[i][0]*matxy[0][0]+vertex2[i][1]*matxy[1][0]+vertex2[i][2]*matxy[2][0]
			vertex2[i][1]=vertex2[i][0]*matxy[0][1]+vertex2[i][1]*matxy[1][1]+vertex2[i][2]*matxy[2][1]
			vertex2[i][2]=vertex2[i][0]*matxy[0][2]+vertex2[i][1]*matxy[1][2]+vertex2[i][2]*matxy[2][2]
    	
	elif (choice==2):
		for i in range(n):
			vertex1[i][0]=vertex1[i][0]*matyz[0][0]+vertex1[i][1]*matyz[1][0]+vertex1[i][2]*matyz[2][0]
			vertex1[i][1]=vertex1[i][1]*matyz[0][1]+vertex1[i][1]*matyz[1][1]+vertex1[i][2]*matyz[2][1]
			vertex1[i][2]=vertex1[i][0]*matyz[0][2]+vertex1[i][1]*matyz[1][2]+vertex1[i][2]*matyz[2][2]
			vertex2[i][0]=vertex2[i][0]*matyz[0][0]+vertex2[i][1]*matyz[1][0]+vertex2[i][2]*matyz[2][0]
			vertex2[i][1]=vertex2[i][0]*matyz[0][1]+vertex2[i][1]*matyz[1][1]+vertex2[i][2]*matyz[2][1]
			vertex2[i][2]=vertex2[i][0]*matyz[0][2]+vertex2[i][1]*matyz[1][2]+vertex2[i][2]*matyz[2][2]
    	
	else:
		for i in range(n):
			vertex1[i][0]=vertex1[i][0]*matxz[0][0]+vertex1[i][1]*matxz[1][0]+vertex1[i][2]*matxz[2][0]
			vertex1[i][1]=vertex1[i][1]*matxz[0][1]+vertex1[i][1]*matxz[1][1]+vertex1[i][2]*matxz[2][1]
			vertex1[i][2]=vertex1[i][0]*matxz[0][2]+vertex1[i][1]*matxz[1][2]+vertex1[i][2]*matxz[2][2]
			vertex2[i][0]=vertex2[i][0]*matxz[0][0]+vertex2[i][1]*matxz[1][0]+vertex2[i][2]*matxz[2][0]
			vertex2[i][1]=vertex2[i][0]*matxz[0][1]+vertex2[i][1]*matxz[1][1]+vertex2[i][2]*matxz[2][1]
			vertex2[i][2]=vertex2[i][0]*matxz[0][2]+vertex2[i][1]*matxz[1][2]+vertex2[i][2]*matxz[2][2]
	draw3dobj(vertex1,vertex2,color2,n,win)
	win.getMouse()
	win.close()
main()