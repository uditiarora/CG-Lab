from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
xc=0
yc=0
r=0
cube1=0
cube2=0

cube1 = [[-80,-80,-100],[-180,-80,-100],[-180,-180,-100],[-80,-180,-100],[-60,-60,0],[-160,-60,0],[-160,-160,0],[-60,-160,0]]
cube2 =[]
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	glOrtho(-500.0,500.0,-500.0,500.0,-500.0,500.0)
	glEnable(GL_DEPTH_TEST)

def init2D(r,g,cube2):
	glClearColor(r,g,cube2,0.0)    
	glMatrixMode (GL_PROJECTION)
	gluOrtho2D (-200.0, 200.0, -200.0, 200.0)


def rotation(s,x):
	if(x==0):
		for i in range(len(cube1)):
			p=cube1[i][0]
			q=cube1[i][1]*math.cos(s) - cube1[i][2]*math.sin(s)
			r=cube1[i][1]*math.sin(s) + cube1[i][2]*math.cos(s)
			d =[p,q,r]
			cube2.append(d)
	if(x==1):
		for i in range(len(cube1)):
			p=cube1[i][2]*math.sin(s) + cube1[i][0]*math.cos(s)
			q=cube1[i][1]
			r=cube1[i][2]*math.cos(s) - cube1[i][0]*math.sin(s)
			d =[p,q,r]
			cube2.append(d)
	if(x==2):
		for i in range(len(cube1)):
			p=cube1[i][0]*math.cos(s) - cube1[i][1]*math.sin(s)
			q=cube1[i][0]*math.sin(s) + cube1[i][1]*math.cos(s)
			r=cube1[i][2]
			d =[p,q,r]
			cube2.append(d)

def translation(tx,ty,tz):
	c =[tx,ty,tz]
	for i in range(len(cube1)):
		d=[]
		for j in range(0,3):
			p=cube1[i][j]+c[j]
			d.append(p)
		cube2.append(d)

def scal(sx,sy,sz):
	c =[sx,sy,sz]
	for i in range(len(cube1)):
		d=[]
		for j in range(0,3):
			p=cube1[i][j]*c[j]
			d.append(p)
		cube2.append(d)


def draw(arr):
	glColor3f(0.3,0.5,0.2)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0][0],arr[0][1],arr[0][2])
	glVertex3f(arr[1][0],arr[1][1],arr[1][2])
	glVertex3f(arr[2][0],arr[2][1],arr[2][2])
	glVertex3f(arr[3][0],arr[3][1],arr[3][2])
	glEnd()

	i=0
	glColor3f(0.6,0.6,0.5)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0+i][0],arr[0+i][1],arr[0+i][2])
	glVertex3f(arr[1+i][0],arr[1+i][1],arr[1+i][2])
	glVertex3f(arr[5+i][0],arr[5+i][1],arr[5+i][2])
	glVertex3f(arr[4+i][0],arr[4+i][1],arr[4+i][2])
	glEnd()
	
	glColor3f(0.2,0.2,0.7)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0][0],arr[0][1],arr[0][2])
	glVertex3f(arr[3][0],arr[3][1],arr[3][2])
	glVertex3f(arr[7][0],arr[7][1],arr[7][2])
	glVertex3f(arr[4][0],arr[4][1],arr[4][2])
	glEnd()

	i=1
	glColor3f(0.5,0.4,0.5)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0+i][0],arr[0+i][1],arr[0+i][2])
	glVertex3f(arr[1+i][0],arr[1+i][1],arr[1+i][2])
	glVertex3f(arr[5+i][0],arr[5+i][1],arr[5+i][2])
	glVertex3f(arr[4+i][0],arr[4+i][1],arr[4+i][2])
	glEnd()


	i=2
	glColor3f(0.5,0.6,0.5)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0+i][0],arr[0+i][1],arr[0+i][2])
	glVertex3f(arr[1+i][0],arr[1+i][1],arr[1+i][2])
	glVertex3f(arr[5+i][0],arr[5+i][1],arr[5+i][2])
	glVertex3f(arr[4+i][0],arr[4+i][1],arr[4+i][2])
	glEnd()

	i=4
	glColor3f(0.3,0.3,0.4)
	glBegin(GL_POLYGON)
	glVertex3f(arr[0+i][0],arr[0+i][1],arr[0+i][2])
	glVertex3f(arr[1+i][0],arr[1+i][1],arr[1+i][2])
	glVertex3f(arr[2+i][0],arr[2+i][1],arr[2+i][2])
	glVertex3f(arr[3+i][0],arr[3+i][1],arr[3+i][2])
	glEnd()

def start():

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	

	glBegin(GL_LINES)
	glColor3f(0,0,0)
	glVertex2i(0,500)
	glVertex2i(0,-500)
	glEnd()

	glBegin(GL_LINES)
	glColor3f(0.0,0.0,0.0)
	glVertex2i(500,0)
	glVertex2i(-500,0)
	glEnd()

	print(cube1)
	print(cube2)
	draw(cube1)
	draw(cube2)
	glFlush()
	


print("Enter your choice: ")
print("1.Tranlation\n2.Scaling\n3.Rotation\n")
n = int(input())

if(n==1):
	print("Enter translation factor tx ty tz: ")
	tx=int(input())
	ty=int(input())
	tz=int(input())
	translation(tx,ty,ty)


elif(n==2):
	print("Enter Scaling factor sx sy sz : ")
	sx=int(input())
	sy=int(input())
	sz=int(input())
	scal(sx,sy,sz)
	

elif(n==3):
	print("Enter Rotation Angle and axis (0 for x,1 for y,2 for z : ")
	s = int(input())
	ax=int(input())
	rotation(math.radians(s),ax)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500,500)
glutInitWindowPosition(100,100)
glutCreateWindow("3d transformation")
init()
glutDisplayFunc(start)
glutMainLoop()
