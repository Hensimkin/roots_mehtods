import sympy as sp
from sympy.utilities.lambdify import lambdify

def polynom(x):
    return (x**4)+(x**3)-(3*(x**2))


def Bisection_Method(polynom,start_point,end_point,eps):
    z=polynom
    bigarray=[]
    size=(abs(start_point)+abs(end_point))/0.1
    num=start_point
    for i in range(int(size)+1):
        smallarray = []
        smallarray.append(num)
        smallarray.append(round(polynom(num),4))
        bigarray.append(smallarray)
        num = num + 0.1
        num=round(num,3)

    for i in range(1,int(size),1):
        if (bigarray[i][1]*bigarray[i-1][1])<0:
            print("I", "   ", "A", "   ", "B", "   ", "C", "   ", "F(a)", "   ", "F(b)", "   ", "F(c)")
            Bisection(polynom, bigarray[i-1][0], bigarray[i][0], eps)
    x = sp.symbols('x')
    f2 = diff(polynom)
    f3 = lambdify(x, f2)
    for i in range(int(size)+1):
        num=round(bigarray[i][0],6)
        f4=round(f3(num),6)
        bigarray[i].append(f4)

    for i in range(1, int(size)+1, 1):
        if (bigarray[i][2] * bigarray[i - 1][2]) < 0:
            print("I", "   ", "A", "   ", "B", "   ", "C", "   ", "F'(a)", "   ", "F'(b)", "   ", "F'(c)")
            Bisection(f3, bigarray[i - 1][0], bigarray[i][0], eps)


def diff(polynom):
    x = sp.symbols('x')
    my_f = polynom(x)
    return sp.diff(my_f, x)




def Bisection(polynom,a,b,eps):
    c=0
    fc=0
    i=1
    counter=0
    temp=0
    while(abs(a-b) >eps):
        c=round((a+b)/2,6)
        fc=round(polynom(c),6)
        if fc<0 and polynom(a)<0:
            temp=round(a,6)
            counter=1
            a=c
            a=round(a,6)
        if fc<0 and polynom(b)<0:
            temp=round(b,6)
            counter=2
            b=c
            b = round(b, 6)
        if fc>0 and polynom(a)>0:
            temp=round(a,6)
            counter=1
            a=c
            a = round(a, 6)
        if fc>0 and polynom(b)>0:
            temp = round(b, 6)
            counter=2
            b=c
            b = round(b, 6)
        if counter==1:
            print(i, " ", temp, " ", b, " ", c, " ", round(polynom(temp),6), " ", round(polynom(b),6), " ", round(fc,6))
        if counter==2:
            print(i, " ", a, " ", temp, " ", c, " ", round(polynom(a),6), " ", round(polynom(temp),6), " ", round(fc,6))
        i+=1
    print("The point is: ",c)


Bisection_Method(polynom,-3,2,0.0001)