from graphics import *
import time

INSIDE = 0 
LEFT = 1    
RIGHT = 2   
BOTTOM = 4  
TOP = 8     

def computeCode(x, y): 
    code = INSIDE 
    if x < xmin:     
        code |= LEFT 
    elif x > xmax:   
        code |= RIGHT 
    if y < ymin:     
        code |= BOTTOM 
    elif y > ymax:    
        code |= TOP 
  
    return code 
    
def cohen(x1,y1,x2,y2,clipWin):
	code1 = computeCode(x1, y1)
	code2 = computeCode(x2, y2)
	accept = False
	while True:
		if code1 == 0 and code2 == 0:
			accept = True
			break
		elif (code1 & code2) != 0:
			break
		else:
			x= 1.0
			y = 1.0
			if code1 != 0:
				code_out = code1
			else:
				code_out = code2
			if code_out & TOP:
				x = x1 + (x2 - x1) *(ymax - y1) / (y2 - y1)
				y= ymax
			elif code_out & BOTTOM:
				x = x1 + (x2 - x1) *(ymin - y1) / (y2 - y1)
				y = ymin
			if code_out & RIGHT:
				y = y1 + (y2 - y1) *(xmax - x1) / (x2 - x1)
				x = xmax
			elif code_out & LEFT:
				y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
				x = xmin
			if code_out == code1:
				x1 = x
				y1 = y
				code1 = computeCode(x1,y1)
			else:
				x2 = x
				y2 = y
				code2 = computeCode(x2, y2)
	if accept:
		print ("Line : %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
		line1 = Line(Point(x1,y1),Point(x2,y2))
		line1.draw(win)
	else:
		print("Line rejected") 
  


	
	

win=GraphWin("Window1",600,600)
win.setCoords(-300,-300,300,300)
xaxis=Line(Point(-300,0),Point(300,0))
yaxis=Line(Point(0,-300),Point(0,300))
xaxis.draw(win)
yaxis.draw(win)

msg = Text(Point(0,0), "(0,0)")
msg.draw(win)

clipWin = [[-100,-100],[100,100]]
xmin,ymin = clipWin[0]
xmax,ymax = clipWin[1]
line1 = Line(Point(xmin,ymin),Point(xmin,ymax))
line1.draw(win)
line1 = Line(Point(xmin,ymin),Point(xmax,ymin))
line1.draw(win)
line1 = Line(Point(xmin,ymax),Point(xmax,ymax))
line1.draw(win)
line1 = Line(Point(xmax,ymax),Point(xmax,ymin))
line1.draw(win)
cohen(-200,-200,50,70,clipWin)


time.sleep(20)






