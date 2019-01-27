import transform


def __main():
	print("Enter minimum co-ordinates of window")
	wx1 = int(input())
	wy1 = int(input())
	print("Enter maximum co-ordinates of window")
	wx2 = int(input())
	wy2 = int(input())
	print("Enter minimum co-ordinates of viewport")
	vx1 = int(input())
	vy1 = int(input())
	print("Enter maximum co-ordinates of viewport")
	vx2 = int(input())
	vy2 = int(input())
	coords = [wx1,wy1,wx2,wy2,vx1,vy1,vx2,vy2]
	print(transform.transformPoint(coords,0,0))
	
	
__main()
