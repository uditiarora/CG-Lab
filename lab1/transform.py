
def transformPoint(coords,px,py):
	wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2 = coords
	qx = vx1 + (px - wx1)*(vx2-vx1)/(wx2 - wx1)
	qy = vy1 + (py - wy1)*(vy2-vy1)/(wy2 - wy1)
	return qx,qy



