import math
import sympy as sym
from sympy import sin,cos,tan,N

print("BOUNDING PHASE METHOD")
x = sym.Symbol('x')


### Function ###

f = x**2 + 10

################

def substitute(k):
    return (f.subs(x,k))

while(1):
    delta = float(input("Enter the delta value : "))
    x_o = 0.6 #initial guess
    x_minus_delta = x_o - delta
    x_plus_delta = x_o + delta
    
    f_minus_delta = substitute(x_minus_delta)
    f_plus_delta = substitute(x_plus_delta)
    f_o = substitute(x_o)
    print("x_minus_delta = {}  x = {}  x_plus_delta = {}".format(x_minus_delta,x_o,x_plus_delta))
    print("f(x-$) = {}  f(x) = {}  f(x+$) = {}".format(f_minus_delta,f_o,f_plus_delta))
    
    if(f_minus_delta>=f_o and f_o>=f_plus_delta):
        delta = delta
        break
    elif(f_minus_delta<=f_o and f_o<=f_plus_delta):
        delta = -delta
        break
    else:
        continue
    

a = []
a.append(x_o)
k = 0
f_o_plus_1 = f_o - 1
while(f_o_plus_1 < f_o):
    x_o_plus_1 = x_o + (2**k)*delta
    a.append(x_o_plus_1)
    k = k + 1
    f_o_plus_1 = substitute(x_o_plus_1)
    f_o = substitute(x_o)
    print("step :", k)
    print("x_o = {} , x_o_plus_1 = {}".format(x_o,x_o_plus_1))
    print("f_o = {}  f_o_plus_1 = {}".format(f_o,f_o_plus_1))
    x_o = x_o_plus_1
  
    
print("( {} , {}  )".format(a[-3],x_o_plus_1))
    
    
    

    