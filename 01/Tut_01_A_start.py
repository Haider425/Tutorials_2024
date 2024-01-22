import numpy as np

def FP(x, a, kMax, epsX, epsF):

    y = map(x, a)      #apply map
    print('Current approximation = ', y)
    
    error = abs(y - x) #compute error
    residual = abs(func(x,a)) #compute residual
    
    if (kMax > 0):  #recusion
        if(error > epsX or residual > epsF):
            x,error,residual = FP(y,a,kMax-1,epsX,epsF)
        else:
            print('Convergence achieved')    
    else:
        print('Maximum number of iterations reached')

    return x,error, residual

def map(x, a):          #Map that produces converging to sqrt(a)
    return 0.5*(x + a/x)

def func(x,a):          #Function to find residual
    return x**2 - a

x, error, residual = FP(3,5,8,1e-6,1e-6)