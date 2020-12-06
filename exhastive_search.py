# exhaustive search
import math
import sympy as sym

print("EXHAUSTIVE SEARCH METHOD")
x = sym.Symbol('x')


### Function ###

f = x**3 + (54/x**2)

################



print("step : 1")
def substitute(k):
    return (f.subs(x,k))

a = float(input("Enter 'a' value "))
b = int(input("Enter 'b' value "))
n = int(input("Enter 'n' value "))
x1 = a
delta_x = (b-a)/n
print(delta_x)
x2 = delta_x + x1
x3 = x2 + delta_x
print("step : 2")
f1 = substitute(x1)
f2 = substitute(x2)
f3 = substitute(x3)
print("x1 = {}  x2 = {}  x3 = {}".format(x1,x2,x3))
print("f1 = {}  f2 = {}  f3 = {}".format(f1,f2,f3))

while (not ((f1 >= f2) and (f2 <= f3))):
    print("step : 2")
    x1=x2
    x2=x3
    x3=x3+delta_x
    print("x1 = {}  x2 = {}  x3 = {}".format(x1,x2,x3))
    f1 = substitute(x1)
    f2 = substitute(x2)
    f3 = substitute(x3)
    print("step : 3")
    if(x3 <= b):
        print("     x3 <= b ----- satisfied ")
        print("f1 = {}  f2 = {}  f3 = {}".format(f1,f2,f3))
        continue
    else:
        print("No minimum lies in {} {}".format(a,b))
        break

print("({} , {})".format(x1,x2+delta_x))
