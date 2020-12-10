import sys
try: 
    import math
    import sympy as sym
    from sympy import sin,cos,tan,N
except:
    print("Packages not installed. Please install 'sympy' package")
    sys.exit()

print("Fibonacci search method")
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
n = float(input("Enter 'n' value ="))
k = 2
l = b - a
iteration = 1

while(1):
    print("\nIteration = ",iteration)
    iteration = iteration + 1
    n_minus_k_plus_1 = n - k + 1
    n_plus_1 = n + 1
    l_k_star = ((sym.fibonacci(n_minus_k_plus_1 + 1)/sym.fibonacci(n_plus_1 + 1))) * l
    x1 = a + l_k_star
    x2 = b - l_k_star
    print("x1 = {} x2 = {}".format(x1,x2))
    f_x1 = substitute(x1)
    f_x2 = substitute(x2)
    print("f_x1 = {} f_x2 = {}".format(f_x1,f_x2))
    if(f_x1 > f_x2):
        a = x1
        print("f_x1 > f_x2")
    elif(f_x1 < f_x2):
        b = x2
        print("f_x1 < f_x2")
    #print(k)
    if( k == n ):
        break
    k = k + 1
    
print("a = {} b = {}".format(a,b))