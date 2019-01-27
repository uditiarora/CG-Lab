
#include <iostream>

#include <graphics.h>

#include <math.h>

#include <conio.h>

using namespace std;

void drawe(int x1, int y1, long a, long b)

{

    long x=0,y=b;

    float p;


    putpixel(x1+getmaxx()/2, getmaxy()/2-y1,1);

    p=2*b*b+a*a*(1-2*b);

    while (y>0)

    {

    if (b*b*x<a*a*y)

    {

        if (p<=a*a/2)

            p+=2*b*b*(3+2*x);

        else

            p+=2*b*b*(3+2*x)-4*a*a*(y-1), y--;

        x++;

    }

    else

    {

        if (p<=b*b/2)

            p+=2*a*a+4*a*a*(y-1);

        else

            p+=2*a*a+4*a*a*(y-1)-4*b*b*(x+1), x++;

        y--;

    }

    putpixel(x+getmaxx()/2+x1,y+getmaxy()/2-y1,5);

    putpixel(-x+getmaxx()/2+x1 ,y+getmaxy()/2-y1,5);

    putpixel(x+getmaxx()/2+x1,-y+getmaxy()/2-y1,5);

    putpixel(-x+getmaxx()/2+x1,-y+getmaxy()/2-y1,5);

    }

}



void main()

{

    int x1, y1, a, b;

    int gdriver = DETECT, gmode, errorcode;

    initgraph(&gdriver, &gmode, "");

    line(0,getmaxy()/2,getmaxx(),getmaxy()/2);

    line(getmaxx()/2,0,getmaxx()/2,getmaxy());

    cout<<"Enter x1 ";

    cin>>x1;

    cout<<"Enter y1 ";

    cin>>y1;

    cout<<"Enter a ";

    cin>>a;

    cout<<"Enter b ";

    cin>>b;

    drawe(x1,y1,a,b);

    getch();

}
