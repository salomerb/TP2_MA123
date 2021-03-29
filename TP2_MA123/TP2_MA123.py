from math import sin 
from math import log
import math

#Question 1

def PointFixe (g,x0,epsilon,Nitermax): 
    xold = x0
    xnew = g(xold)
    n = 1

    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = g(xold)
        n = n+1
    return xnew, n, abs(xnew - xold)
   
#Question 2

def g1(x):
    return (9-3*x)**(1/4)
def g1n(x):
    return -(9-3*x)**(1/4)

def g2(x):
    return math.acos((x+2)/3)
def g2n(x):
    return -math.acos((x+2)/3)

def g3(x):
    return log(7/x)

def g5(x):
    return math.atan((x+5)/2)

def g6(x):
    return log((x**2)+3)

def g7(x):
    return (7-4*log(x))/3

def g8(x):
    return (2*(x**2)-4*x+17)**(1/4)
def g8n(x):
    return -(2*(x**2)-4*x+17)**(1/4)

def g9(x): 
    return log(7+2*sin(x))

def g10(x):
    return log(10/log((x**2)+4))

print (PointFixe(g1,0,1e-10,5e4))
print (PointFixe(g1n,0,1e-10,5e4))
print (PointFixe(g2,0,1e-10,5e4))
print (PointFixe(g2n,0,1e-10,5e4))
print (PointFixe(g3,1,1e-10,5e4))
print (PointFixe(g5,0,1e-10,5e4))
print (PointFixe(g6,1,1e-10,5e4))
print (PointFixe(g7,1,1e-10,5e4))
print (PointFixe(g8,0,1e-10,5e4))
print (PointFixe(g8n,0,1e-10,5e4))
print (PointFixe(g9,0,1e-10,5e4))
print (PointFixe(g10,1,1e-10,5e4))