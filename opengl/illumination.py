
import sys 
import time 
from OpenGL import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import math 
window = 0 
width, height=800, 600 
spin=0 
qaAmbientLight = [] 
qaDiffuseLight = [] 
qaSpecularLight = [] 
qaLightPosition = [] 
matDiffuse=[] 
matSpecular=[] 
def init(): 
	glClearColor(1.0,1.0,1.0,0.0) 
	glEnable(GL_DEPTH_TEST) 
	glMatrixMode(GL_PROJECTION) 
	glLoadIdentity() 
	glOrtho(-2.0, 2.0, -2.0, 2.0, -5.0, 5.0) 
	#Lighting set up 
	glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE) 
	glEnable(GL_LIGHTING) 
	glEnable(GL_LIGHT0) 
	#set Lighting intensity and color 
	glLightfv(GL_LIGHT0, GL_AMBIENT, qaAmbientLight) 
	glLightfv(GL_LIGHT0, GL_DIFFUSE, qaDiffuseLight) 
	glLightfv(GL_LIGHT0, GL_SPECULAR, qaSpecularLight) 
def display(): 
	global spin 
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
	#set light position 
	glLightfv(GL_LIGHT0, GL_POSITION, qaLightPosition) 
	glEnable(GL_DEPTH_TEST) 
	#set material properties 
	qaBlack=[0.0,0.0,0.0,0.0] 
	qaLowAmbient = [0.2, 0.2, 0.2, 1.0] 
	qaFullAmbient = [1.0, 1.0, 1.0, 1.0] 
	if model==1: 
		glShadeModel(GL_FLAT) 
	else: 
		glShadeModel(GL_SMOOTH) 
	#Set, ambient, diffuse and specular lighting. 
	qaFullAmbient = [1.0, 1.0, 1.0, 1.0] 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, matDiffuse) 
	glMaterialfv(GL_FRONT, GL_SPECULAR, matSpecular) 
	glMaterialf(GL_FRONT, GL_SHININESS, matShininess) 
	glLightfv(GL_LIGHT0, GL_AMBIENT, qaLowAmbient) 
	glMatrixMode(GL_MODELVIEW) 
	glLoadIdentity() 
	glPushMatrix() 
	glTranslatef(0.0, 0.0, 0.5) 
	glPushMatrix() 
	glRotatef(spin,1.0,0.0,0.0) 
	glLightfv (GL_LIGHT0, GL_POSITION, qaLightPosition) 
	glTranslatef (qaLightPosition[0], qaLightPosition[1], qaLightPosition[2]) 
	glDisable (GL_LIGHTING) 
	glColor3f (0.0, 0.0, 0.0) 
	#draw light as cube 
	glutWireCube (0.1) 
	glEnable (GL_LIGHTING) 
	glPopMatrix () 
	#draw object 
	glutSolidSphere (0.475, 80, 150) 
	glPopMatrix () 
	#Turn off diffuse and specular reflection 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, qaBlack) 
	glMaterialfv(GL_FRONT, GL_SPECULAR, qaBlack) 
	glLightfv(GL_LIGHT0, GL_AMBIENT, qaFullAmbient) 
	glFlush() 
def mouse(button,state,x,y): 
global spin 
if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN: 
spin=(spin+30)%360 
glutPostRedisplay() 
def main(): 
file=open("inputLight.txt","r") 
line=0 
for each in file: 
if line==1: 
x, y, z, a=each.split() 
qaAmbientLight.append(float(x)) 
qaAmbientLight.append(float(y)) 
qaAmbientLight.append(float(z)) 
qaAmbientLight.append(float(a)) 
elif line==2: 
x, y, z, a=each.split() 
qaDiffuseLight.append(float(x)) 
qaDiffuseLight.append(float(y)) 
qaDiffuseLight.append(float(z)) 
qaDiffuseLight.append(float(a)) 
elif line==3: 
x, y, z, a=each.split() 
qaSpecularLight.append(float(x)) 
qaSpecularLight.append(float(y)) 
qaSpecularLight.append(float(z)) 
qaSpecularLight.append(float(a)) 
elif line==4: 
x, y, z, a=each.split() 
qaLightPosition.append(float(x)) 
qaLightPosition.append(float(y)) 
qaLightPosition.append(float(z)) 
qaLightPosition.append(float(a)) 
elif line==6: 
x, y, z, a=each.split() 
matDiffuse.append(float(x)) 
matDiffuse.append(float(y)) 
matDiffuse.append(float(z)) 
matDiffuse.append(float(a)) 
elif line==7: 
x, y, z, a=each.split() 
matSpecular.append(float(x)) 
matSpecular.append(float(y)) 
matSpecular.append(float(z)) 
matSpecular.append(float(a)) 
elif line==8: 
global matShininess 
matShininess=float(each) 
elif line==10: 
global model 
model=int(each) 
line+=1 
glutInit(sys.argv) 
glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE|GLUT_ALPHA|GLUT_DEPT H) 
glutInitWindowSize(width, height) 
glutInitWindowPosition(0,0) 
glutCreateWindow(b'SHADING') 
glutDisplayFunc(display) 
#glutSpecialFunc(processSpecialKeys) 
glutMouseFunc(mouse) 
init() 
glutMainLoop() 
main() 


