#include<stdio.h>
#include<graphics.h>
#include<stdlib.h>
#include<conio.h>
 
#define MAX 20
 
void swap(int* a,int* b)
{
	int t=*a;
	*a=*b;
	*b=t;
}
 
void midpointline(int x1,int y1,int x2,int y2)
{
	int dx,dy,d,incry,incre,incrne,slopegt1=0;
	dx=abs(x1-x2);dy=abs(y1-y2);
	if(dy>dx)
	{
		swap(&x1,&y1);
		swap(&x2,&y2);
		swap(&dx,&dy);
		slopegt1=1;
	}
	if(x1>x2)
	{
		swap(&x1,&x2);
		swap(&y1,&y2);
	}
	if(y1>y2)
		incry=-1;
	else
		incry=1;
	d=2*dy-dx;
	incre=2*dy;
	incrne=2*(dy-dx);
	while(x1<x2)
	{
		if(d<=0)
			d+=incre;
		else
		{
			d+=incrne;
			y1+=incry;
		}
		x1++;
		if(slopegt1)
			putpixel(y1,x1,WHITE);
		else
			putpixel(x1,y1,WHITE);
	}
}
 
void main()
{
	int n,i;
	int pt[MAX][2];
	int gd=DETECT,gm;
 
	printf("Enter the number of points:");
	scanf("%d",&n);
 
	printf("Enter the x and y coordinates:");
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&pt[i][0],&pt[i][1]);
		pt[i][1]=480 - pt[i][1];
	}
 
	initgraph(&gd,&gm,"..\\bgi");
 
	line(1,0,1,480);		// X - Axis
	line(0,479,639,479);		// Y - Axis
 
	outtextxy(pt[0][0]-2,pt[0][1]-3,"*");
 
	for(i=0;i<n-1;i++)
	{
		midpointline(pt[i][0],pt[i][1],pt[i+1][0],pt[i+1][1]);
		outtextxy(pt[i+1][0]-2,pt[i+1][1]-3,"*");
	}
	getch();
	closegraph();
}
