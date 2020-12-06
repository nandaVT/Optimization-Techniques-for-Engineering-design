import sys
try: 
    import math
    import sympy as sym
    from sympy import sin,cos,tan,N
except:
    print("Packages not installed. Please install 'sympy' package")
    sys.exit()

print("Box Evolutionary method")
x = sym.Symbol('x')
y = sym.Symbol('y')

def substitute(pt):
    return (f.subs([(x,pt[0]),(y,pt[1])]))

while(True):
    s = ""
    func = input("Enter the function = ")  #x-y+2*(x**2)+2*x*y+y**2
    for i in func:
        s= s+i
        
    try:
        exec("f = "+s)
        break
    except:
        print("Entered function is incompatible. Try again.")
        
E = float(input("Enter the epsilon 'E' value = "))  #0.4
x_o = list(map(float,input("Enter the x_o value (give only space between the values) =  ").split()))  #[1,0]
delta = list(map(float,input("Enter the delta value (give only space between the values) =  ").split()))#[1,1]
iteration = 1

def mod_epsilon(arr):
    return math.sqrt(arr[0]**2+arr[1]**2)

while(mod_epsilon(delta) > E):
    print("\niteration = ",iteration)
    iteration = iteration + 1
    print("x_o = {}  delta = {} ==> mod_epsilon = {}".format(x_o,delta,mod_epsilon(delta)))
    x1 = [x_o[0] + delta[1]/2, x_o[1] + delta[1]/2]
    x2 = [x_o[0] + delta[1]/2, x_o[1] - delta[1]/2]
    x3 = [x_o[0] - delta[1]/2, x_o[1] + delta[1]/2]
    x4 = [x_o[0] - delta[1]/2, x_o[1] - delta[1]/2]
    print("x1 = {} x2 = {} x3 = {} x4 = {}".format(x1,x2,x3,x4))
    f_o = substitute(x_o)
    f1 = substitute(x1)
    f2 = substitute(x2)
    f3 = substitute(x3)
    f4 = substitute(x4)
    print("f1 = {} f2 = {} f3 = {} f4 = {}".format(f1,f2,f3,f4,f_o))
    min_f = min(f1,f2,f3,f4,f_o)
    if(min_f == f_o):
        delta[0] = delta[0]/2
        delta[1] = delta[1]/2
        print("minimum = ",x_o)
    elif(min_f == f1):
        x_o = x1
        print("minimum = ",x1)
    elif(min_f == f2):
        x_o = x2
        print("minimum = ",x2)
    elif(min_f == f3):
        x_o = x3
        print("minimum = ",x3)
    elif(min_f == f4):
        x_o = x4
        print("minimum = ",x4)
        
print(x_o)
    