import sympy as sym
from sympy import sin,cos,tan,N

print("********* TO EXIT PRESS 'q' **********")
x = sym.Symbol('x')

def substitute(k):
    return (f.subs(x,k))

while(True):
    s = ""
    func = input("Enter the function = ")
    for i in func:
        s= s+i
        
    try:
        exec("f = "+s)
        break
    except:
        print("Entered function is incompatible. Try again.")

while(True):
    
    n = input("Enter the variable = ")
    if(n == 'q'):
        break
    print(N(substitute(n)))

