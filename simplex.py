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
    func = "x-y+(2*x**2)+2*x*y+y**2" #input("Enter the function = ")
    for i in func:
        s= s+i
        
    try:
        exec("f = "+s)
        print(f)
        break
    except:
        print("Entered function is incompatible. Try again.")
        
x1 = list(map(float,input("Enter the initial x1 point value (give only space between the values) =  ").split()))   #[4,4]
x2 = [x1[0]+1,x1[1]]
x3 = [x1[0],x1[1]+1]
beta = float(input("Enter the beta value = ")) #0.5
gamma = float(input("Enter the gamma value = ")) #2.0
epsilon = float(input("Enter the epsilon value = ")) #2.0
q = epsilon + 1
iteration = 1
x_c=[]


while(q > epsilon):
    print("\niteration = ",iteration)
    iteration = iteration + 1
    print("x1 = {} x2 = {} x3 = {}".format(x1,x2,x3))
    f1 = substitute(x1)
    f2 = substitute(x2)
    f3 = substitute(x3)
    print("f1 = {} f2 = {} f3 = {}".format(f1,f2,f3))
    x_n = [x1,x2,x3]
    f_n = [f1,f2,f3]
    x_h = x_n[f_n.index(max(f1,f2,f3))]
    x_l = x_n[f_n.index(min(f1,f2,f3))]
    x_o = [(x1[0]+x2[0]+x3[0]-x_h[0])/2,(x1[1]+x2[1]+x3[1]-x_h[1])/2]
    x_r = [2*x_o[0]-x_h[0],2*x_o[1]-x_h[1]]
    f_r = substitute(x_r)
    f_l = substitute(x_l)
    print("x_h = {} x_l = {} x_o = {} x_r = {} ".format(x_h,x_l,x_o,x_r))
    if(f_r < f_l):
        print("f_r < f_l")
        x_e = [gamma*x_r[0]+(1-gamma)*x_o[0],gamma*x_r[1]+(1-gamma)*x_o[1]]
        f_e = substitute(x_e)
        print("x_e = {} f_e = {}".format(x_e,f_e))
        if(f_e < f_r):
            print("f_e < f_r")
            if(x1 == x_h):
                x1 = x_e[:]
                print("replace x1 by x_h")
            elif(x2 == x_h):
                x2 = x_e[:]
                print("replace x2 by x_h")
            elif(x3 == x_h):
                x3 = x_e[:]
                print("replace x3 by x_h")
        elif(f_e > f_r):
            print("f_e > f_r")
            if(x1 == x_h):
                x1 = x_r[:]
                print("replace x1 by x_r")
            elif(x2 == x_h):
                x2 = x_r[:]
                print("replace x2 by x_r")
            elif(x3 == x_h):
                x3 = x_r[:]
                print("replace x3 by x_r")
    elif(f_r > f_l or f_r > f_h):
        print("f_r > f_l")
        x_c = [beta*x_h[0] + (1-beta)*x_o[0],beta*x_h[1] + (1-beta)*x_o[1]]
        f_c = substitute(x_c)
        print(x_c)
        if(x1 == x_h):
            x1 = x_c[:]
            print("replace x1 by x_c")
        elif(x2 == x_h):
            x2 = x_c[:]
            print("replace x2 by x_c")
        elif(x3 == x_h):
            x3 = x_c[:]
            print("replace x3 by x_c")
    
    f1 = substitute(x1)
    f2 = substitute(x2)
    f3 = substitute(x3)
    f_o = substitute(x_o)
    q = math.sqrt(((f1-f_o)**2 + (f2 - f_o)**2 + (f3 - f_o)**2)/3 )
    print("q = ",q)
    