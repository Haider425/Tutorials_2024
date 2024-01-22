def FP(x, a, kMax, epsX, epsF):
    for k in range(1, kMax + 1):  # recusion
        ck = (x[0] + x[1]) / 2
        fk = F(ck, a)

        if fk * F(x[0], a) > 0:  # update interval
            x[0] = ck
        else:
            x[1] = ck

        if abs(x[1] - (x[0] + x[1]) / 2) < epsX or abs(fk) < epsF:  # convergence
            break

    x_star = (x[0] + x[1]) / 2 # final approximation
    error = abs(x[1] - x[0])   # compute error
    residual = fk              # compute residual

    return x_star, error, residual

def F(x, a):
    val = x**2 - 2 - a  # function to find residual
    return val

x, error, residual = FP([3, 5], 5, 8, 1e-6, 1e-6)  # initial approximation

# print results
print('x = ', x)  
print('error = ', error)
print('residual = ', residual)
