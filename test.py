import sympy as sym
from sympy import sin,cos,tan,N

print("Testing ")
x = sym.Symbol('x')

def substitute(k):
    return (f.subs(x,k))

n = ""
s = ""
func = input("Enter the func = ")
for i in func:
    s= s+i
exec("f = "+s)
#f = eval(func,{"x": x ,"cos" : cos , "N" : N ,"sin" : sin ,"tan" : tan , "n" : n })


while(True):
    
    n = input("Enter the variable = ")
    if(n == 'q'):
        break
    print(N(substitute(n)))

