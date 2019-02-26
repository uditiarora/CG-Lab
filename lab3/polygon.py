from graphics import *
import time
import math
origin = [0, 0]
refvec = [0, 1]

def clockwiseangle_and_distance(point):
    vector = [point[0]-origin[0], point[1]-origin[1]]
    lenvector = math.hypot(vector[0], vector[1])
    if lenvector == 0:
        return -math.pi, 0
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
    	return 2*math.pi+angle, lenvector
    return angle, lenvector
    
def getx(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num//den
def gety(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num//den
	
	
def util(polygon,clipWindow,x1,y1,x2,y2):
	new_points = []
	n = len(polygon)
	for i in range(n):
		k = (i+1)%n
		kx,ky = polygon[k][0],polygon[k][1]
		ix,iy = polygon[i][0],polygon[i][1]
		i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
		k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)
		if(i_pos<0 and k_pos<0):
			new_points.append([kx,ky])
		elif(i_pos>=0 and k_pos<0):
			tempx = getx(x1,y1,x2,y2,ix,iy,kx,ky)
			tempy = gety(x1,y1,x2,y2,ix,iy,kx,ky)
			new_points.append([tempx,tempy])
			new_points.append([kx,ky])
		elif(i_pos<0 and k_pos>=0):
			tempx = getx(x1,y1,x2,y2,ix,iy,kx,ky)
			tempy = gety(x1,y1,x2,y2,ix,iy,kx,ky)
			new_points.append([tempx,tempy])
	print(new_points)
	return new_points
def clip(polygon,clipWindow):
	n = len(clipWindow)
	for i in range(n):
		k = (i+1)%n
		polygon = util(polygon,clipWindow,clipWindow[i][0],clipWindow[i][1],clipWindow[k][0],clipWindow[k][1])
	return polygon
    
   
win=GraphWin("Window1",600,600)
win.setCoords(-300,-300,300,300)
xaxis=Line(Point(-300,0),Point(300,0))
yaxis=Line(Point(0,-300),Point(0,300))
xaxis.draw(win)
yaxis.draw(win)

msg = Text(Point(0,0), "(0,0)")
msg.draw(win)

polygon =  [[100,150], [200,250], [300,200] ]
clipWindow =  [[150,150], [150,200], [200,200], [200,150]]
for i in range(len(clipWindow)-1):
	p1 = Point(clipWindow[i][0],clipWindow[i][1])
	p2 = Point(clipWindow[i+1][0],clipWindow[i+1][1])
	line = Line(p1,p2)
	line.draw(win)

p1 = Point(clipWindow[0][0],clipWindow[0][1])
p2 = Point(clipWindow[len(clipWindow)-1][0],clipWindow[len(clipWindow)-1][1])
line = Line(p1,p2)
line.draw(win)

list1 = clip(polygon,clipWindow)
print("Final list",list1)

#list2 = sorted(list1, key=clockwiseangle_and_distance)
m = len(list1)
for i in range(m):
	k = (i+1)%m
	p1 = Point(list1[i][0],list1[i][1])
	p2 = Point(list1[k][0],list1[k][1])
	line = Line(p1,p2)
	line.draw(win)


time.sleep(10)




