# Speed test: computing the determinant recursively or with LU decomposition.
# Starter code by L van Veen, Ontario Tech U, 2024.
import numpy as np
import time                              # For timing
import matplotlib.pyplot as plt
from LU import LU
from deter_starter_code import deter

# Consider matrices of size n X n where n=istart .. iend with recursive computation:
istart = 2
iend = 10
wtimerec= np.zeros((iend-istart+1,2))       # Array to store wall times.      
for n in range(istart,iend+1):
    A = np.random.rand(n,n)                  # Initialize random matrix.
    start = time.time()                       # Start timer.
    detA = deter(A)                                   # Computation using cofactor expansion.
    elapsed = time.time() - start                                 # Measure elapsed time.
    print("n=%d wall time=%f det=%e" %(n,elapsed,detA))         # Output value of determinant.
    wtimerec[i-istart,0]=n                   # store data for plotting
    wtimerec[i-istart,1]=elapsed

# Consider matrices of size n X n where n=istart .. iend with LU decomposition:
istart = 2
iend = 10
wtimeLU=np.zeros((iend-istart+1,2))       
for n in range(istart,iend+1):
    A = np.random.rand(n,n)                  # Initialize random matrix.
    start = time.time()                       # Start timer.
    L,U,ok = LU(A)                           # LU-decompose A=P^t LU.
    if ok==1:
        detA = deter(U)                               # Compute determinant from diagonal of U.
        elapsed = time.time() - start                            # Measure elapsed time.
        print("n=%d wall time=%f det=%e" %(n,elapsed,detA))         # Output value of determinant.
        wtimeLU[n-istart,0]=n                # Store data for plotting.
        wtimeLU[n-istart,1]=elapsed
    else:
        print("Near-zero pivot in LU decomposition for n=%d\n" % (n))

plt.loglog(wtimerec[:,0],wtimerec[:,1],'-*r', label='recursive')
plt.loglog(wtimeLU[:,0],wtimeLU[:,1],'-*g', label='using LUP')
plt.loglog(wtimeLU[:,0],1e-6*wtimeLU[:,0]**3,'-k', label='n^3')
plt.legend()
plt.show()
