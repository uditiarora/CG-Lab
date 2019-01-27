import time
from graphics import*


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
		xwithyminTS = x2
	else:
		scanline = y1
		ymaxTS = y2
		xwithyminTS = x1
	storeEdgeInTuple(edgeTable[scanline],ymaxTS,xwithyminTS,minv)
	print(ymaxTS,xwithyminTS,minv)
	"""
	edgeTable[scanline].buckets[edgeTable[scanline].count].ymax = ymaxTS
	edgeTable[scanline].buckets[edgeTable[scanline].count].xofymin = xwithyminTS
	edgeTable[scanline].buckets[edgeTable[scanline].count].slopeinverse = minv
	insertionSort(edgeTable[scanline])
	edgeTable[scanline].count += 1"""
	#print(edgeTable[scanline].buckets[edgeTable[scanline].count].ymax, edgeTable[scanline].buckets[edgeTable[scanline].count].xofymin, edgeTable[scanline].buckets[edgeTable[scanline].count].slopeinverse)
	
def removeEdgeByYmax(tup,yy):
	i = 0
	j = 0
	for i in range(0,tup.count):
		if(tup.buckets[i].ymax == yy):
			for j in range(i,tup.count-1):
				"""tup.buckets[j].ymax = tup.buckets[j+1].ymax
				tup.buckets[j].xofymin = tup.buckets[j+1].xofymin
				tup.buckets[j].slopeinverse = tup.buckets[j+1].slopeinverse"""
				tup.buckets[j].edit_2(tup.buckets[j+1].ymax,tup.buckets[j+1].xofymin,tup.buckets[j+1].slopeinverse)
			#tup.count -= 1
			tup.decCount()
			i -= 1

def updatebyslopeinv(tup):
	i = 0
	for i in range(0,tup.count):
		#tup.buckets[i].xofymin += tup.buckets[i].slopeinverse
		tup.buckets[i].edit_xofymin(tup.buckets[i].slopeinverse)
	 
def scanline():
	i = 0
	j = 0
	x1 = 0
	ymax1 = 0
	x2 = 0
	ymax2 = 0
	fillFlag = 0
	coordCount = 0
	for i in range(0,maxHt):
		for j in range(0,edgeTable[i].count):
			storeEdgeInTuple(activeEdgeTup,edgeTable[i].buckets[j].ymax,edgeTable[i].buckets[j].xofymin, edgeTable[i].buckets[j].slopeinverse)
		removeEdgeByYmax(activeEdgeTup,i)
		insertionSort(activeEdgeTup)
		j = 0
		fillFlag = 0
		coordCount = 0
		x1 = 0
		x2 = 0
		ymax1 = 0
		ymax2 = 0
		while(j<activeEdgeTup.count):
			#print(activeEdgeTup.buckets[j].xofymin)
			if(coordCount%2 == 0):
				x1 = int(activeEdgeTup.buckets[j].xofymin)
				ymax1 = activeEdgeTup.buckets[j].ymax
				if(x1 == x2):
					if(((x1 == ymax1) and x2 != ymax2) or ((x1 != ymax1) and (x2 == ymax2))):
						x2 = x1
						ymax2 = ymax1
					else:
						coordCount += 1
				else:
					coordCount += 1
			else:
				x2 = int(activeEdgeTup.buckets[j].xofymin)
				ymax1 = activeEdgeTup.buckets[j].ymax
				fillFlag = 0
				if(x1 == x2):
					if(((x1 == ymax1) and (x2 != ymax2)) or ((x1 != ymax1) and (x2 == ymax2))):
						x1 = x2
						ymax1 = ymax2
					else:
						coordCount += 1
						fillFlag = 1
				else:
					coordCount += 1
					fillFlag = 1
				if(fillFlag == 1):
					#draw a line here from (x1,i) to (x2,i)
					print(x1,i,x2,i)
					l1 = Line(Point(x1,i),Point(x2,i))

					l1.draw(win)
					time.sleep(0.1)
			j += 1


edgeTable = []

activeEdgeTup = edgeTableTup()

win = GraphWin("polygon",800,600)
points = [[100,200,100,300],[100,300,200,300],[200,300,200,200],[200,200,100,200]]
for i in range(maxHt):
	temp = edgeTableTup()
	edgeTable.append(temp)

for i in range(0,len(points)):
	x1,y1,x2,y2 = points[i]
	l1 = Line(Point(x1,y1),Point(x2,y2))
	l1.setWidth(3)
	l1.draw(win)
	storeEdgeInTable(x1,y1,x2,y2)
scanline()
time.sleep(4)




