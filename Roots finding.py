def polynom(x):
    return (x**4)+(x**3)-(3*(x**2))


def Bisection_Method(polynom,start_point,end_point,eps):
    bigarray=[]
    size=(abs(start_point)+abs(end_point))/0.1
    num=start_point
    for i in range(int(size)):
        smallarray = []
        smallarray.append(num)
        smallarray.append(round(polynom(num),4))
        bigarray.append(smallarray)
        num = num + 0.1
        num=round(num,3)
    for i in range(1,int(size),1):
        if (bigarray[i][1]*bigarray[i-1][1])<0:
            Bisection(polynom, bigarray[i-1][0], bigarray[i][0], eps)
    #for i in range(int(size)):




def Bisection(polynom,a,b,eps):
    num1=0
    num2=0
    c=0
    fc=0
    i=1
    counter=0
    temp=0
    print("I","   ","A","   ","B","   ","C","   ","F(a)","   ","F(b)","   ","F(c)")
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




"""""
Bisection_Method(polynom,-3,2,0.0001)


for i in range(int(size)):
print(i+1," ",end=" ")
for j in range(2):
    print(bigarray[i][j]," ",end=" ")
print( )
"""""
import sympy as sp
x =sp.symbols('x')
my_f=polynom(x)
print("my_func: ",my_f)
my_f1=sp.diff( my_f,x)
print("f' : ",my_f1)
d1=sp.diff(my_f1)
print("f'': ",d1)




from sympy.utilities.lambdify import lambdify
f = (x**4)+(x**3)-(3*(x**2))
f_prime = f.diff(x)
print("f : ",f)
print("f' : ",f_prime)
f = lambdify(x, f)
f_prime = lambdify(x, f_prime)
