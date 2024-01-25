import numpy as np

def secant(f, x0, x1, kMax, epsX, epsF):
    
    record = np.zeros((kMax,3))
    fxp = f(x0) #previous function value
    conv = 0
    
    
    for i in range(kMax):
        fxc = f(x1) #current function value
        dx = -fxc*(x1-x0)/(fxc-fxp)
        x = x1 + dx
        err = abs(dx)
        res = abs(fxc)
        record[i,:] = [i,err,res]
        print('It %d, x=%f, err=%e' % (i,x,err))
        if err < epsX and res < epsF:
            conv = 1
            print('Converged')
            break
        x0 = x1
        x1 = x
        fxp = fxc
        
    if conv == 0:
        print('No convergence in secant.')
    return x,record

def f(x):
    return x**2 - 2

# x,record = secant(f, 1, 2, 100, 1e-6, 1e-6)
# print('x = %f' % x)
