from graphics import *
import time
maxHt = 800
maxWd = 600
maxVer = 10000

class edgeBucket:
	def __init__(self):
		self.ymax = 0
		self.xofymin = 0.0
		self.slopeinverse = 0.0
	def edit_2(self,ym,xm,slopeInv):
		self.ymax = ym
		self.xofymin = xm
		self.slopeinverse = slopeInv
	def edit_xofymin(self,var):
		self.xofymin += var
		
class edgeTableTup:
	def __init__(self):
		self.count = 0
		self.buckets = [edgeBucket() for i in range(maxVer)]
	def edit(self,ym,xm,slopeInv):
		self.buckets[self.count].edit_2(ym,xm,slopeInv)
	def editCount(self):
		self.count += 1
	def decCount(self):
		self.count -= 1

def insertionSort(ett):
	i = 0
	j = 0
	temp = edgeBucket()
	for i in range(1,ett.count):
		"""temp.ymax = ett.buckets[i].ymax
		temp.xofymin = ett.buckets[i].xofymin
		temp.slopeinverse = ett.buckets[i].slopeinverse"""
		temp.edit_2(ett.buckets[i].ymax,ett.buckets[i].xofymin,ett.buckets[i].slopeinverse)
		j = i-1
		while((temp.xofymin < ett.buckets[i].xofymin) and (j>=0)):
			"""ett.buckets[j+1].ymax = ett.buckets[j].max
			ett.buckets[j+1].xofymin = ett.buckets[j].xofymin
			ett.buckets[j+1].slopeinverse = ett.buckets[j].slopeinverse"""
			ett.buckets[j+1].edit_2(ett.buckets[j].ymax,ett.buckets[j].xofymin,ett.buckets[j].slopeinverse)
			j = j-1
		"""ett.buckets[j+1].ymax = temp.ymax
		ett.buckets[j+1].xofymin = temp.xofymin
		ett.buckets[j+1].slopeinverse = temp.slopeinverse"""
		ett.buckets[j+1].edit_2(temp.ymax,temp.xofymin,temp.slopeinverse)

def storeEdgeInTuple(r,ym,xm,slopeInv):
	"""r.buckets[r.count].ymax = ym
	r.buckets[r.count].xyofmin = xm
	r.buckets[r.count].slopeinverse = slopeInv"""
	r.edit(ym,xm,slopeInv)
	insertionSort(r)
	"""r.count += 1"""
	r.editCount()
	
def storeEdgeInTable(x1,y1,x2,y2):	
	m = 0.0
	mvin = 0.0
	ymaxTS = 0
	xwithyminTS = 0
	scanline = 0
	
	if(x2==x1):
		minv = 0.0000
	else:
		m = (float(y2-y1))/(x2-x1)
		if(y2==y1):
			return
		minv = 1.0/m
	if(y1>y2):
		scanline = y2
		ymaxTS = y1
		xwithminTS = x2
	else:
		scanline = y1
		ymaxTS = y2
		xwithminTS = x1
	storeEdgeInTuple(edgeTable[scanline],ymaxTS,xwithyminTS,minv)
	print(ymaxTS,xwithyminTS,minv)
	"""
	edgeTable[scanline].buckets[edgeTable[scanline].count].ymax = ymaxTS
	edgeTable[scanline].buckets[edgeTable[scanline].count].xofymin = xwithyminTS
	edgeTable[scanline].buckets[edgeTable[scanline].count].slopeinverse = minv
	insertionSort(edgeTable[scanline])
	edgeTable[scanline].count += 1"""
	#print(edgeTable[scanline].buckets[edgeTable[scanline].count -1].ymax, edgeTable[scanline].buckets[edgeTable[scanline].count -1].xofymin, edgeTable[scanline].buckets[edgeTable[scanline].count -1].slopeinverse)
"""
def xyz(r,x,y,z):
	r.edit(x,y,z)
	r.editCount()	

obj = edgeTableTup()
#obj.edit(1,2,3)
xyz(obj,1,2,3)
print(obj.buckets[0].ymax, obj.buckets[0].xofymin, obj.buckets[0].slopeinverse)
#obj.editCount()
print(obj.count)"""







edgeTable = []

activeEdgeTup = edgeTableTup()

win = GraphWin("polygon",800,600)
points = [[50,100,75,75],[75,75,75,25],[75,50,50,0],[50,0,25,25],[25,25,25,75],[25,75,50,100]]
for i in range(maxHt):
	temp = edgeTableTup()
	edgeTable.append(temp)

for i in range(0,len(points)):
	x1,y1,x2,y2 = points[i]
	l1 = Line(Point(x1,y1),Point(x2,y2))
	l1.setWidth(3)
	l1.draw(win)
	storeEdgeInTable(x1,y1,x2,y2)




