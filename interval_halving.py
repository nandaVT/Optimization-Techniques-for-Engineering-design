import sys
try: 
    import math
    import sympy as sym
    from sympy import sin,cos,tan,N
except:
    print("Packages not installed. Please install 'sympy' package")
    sys.exit()

print("Interval Halving method")
x = sym.Symbol('x')

def substitute(k):
    return (f.subs(x,k))

while(True):
    s = ""
    func = input("Enter the function = ")    #"x**2+(54/x)"
    for i in func:
        s= s+i
        
    try:
        exec("f = "+s)
        print(f)
        break
    except:
        print("Entered function is incompatible. Try again.")
    
a = float(input("Enter 'a' value = "))
b = float(input("Enter 'b' value = "))
epsilon = float(input("Enter epsilon value ="))
x_m = (a+b)/2
l = b - a
f_x_m = substitute(x_m)
mod_l = sym.sqrt(l**2)
iteration = 1

while(mod_l > epsilon):
    print("Iteration = ",iteration)
    iteration = iteration + 1
    print("a = {} b = {}".format(a,b))
    x_1 = a + l/4
    x_2 = b - l/4
    print("x_1 = {} x_2 = {} x_m = {}".format(x_1,x_2,x_m))
    f_x_m = substitute(x_m)
    f_x_1 = substitute(x_1)
    f_x_2 = substitute(x_2)
    print("f_x_1 = {} f_x_2 = {} f_x_m = {}".format(f_x_1,f_x_2,f_x_m))
    if(f_x_1 < f_x_m):
        b = x_m
        print("f_x_1 < f_x_m")
    if(f_x_1 > f_x_m):
        a = x_1
        print("f_x_1 > f_x_m")
    if(f_x_2 < f_x_m):
        a = x_m
        print("f_x_2 < f_x_m")
    if(f_x_2 > f_x_m):
        b = x_2
        print("f_x_2 > f_x_m")

    l = b - a
    x_m = (a+b)/2
    mod_l = sym.sqrt(l**2)
    print("L = {} mod_L = {} \n".format(l , mod_l))
    
    
print("a = {} b = {}".format(a,b))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    