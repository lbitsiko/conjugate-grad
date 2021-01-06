import numpy as np
import numpy.linalg as LA

def conj_grad(A, x, x0, maxiter=2):
    x = np.copy(x0)
    Ax = np.matmul(A, x)
    r = b - Ax
    p = np.copy(r)
    print("Starting with:")
    print("x_0 = ", x)
    print("r_0 = ", r)
    print("p_0 = ", p)
    print("")
    for k in range(maxiter):
        Ap = np.matmul(A, p)
        norm_p_A = np.dot(p, Ap)
        ak = np.dot(p, r) / norm_p_A
        x += + ak * p
        r += r - ak * Ap
        bk = np.dot(Ap, r) / np.dot(Ap, p)
        p = r - bk * p

        print("a_{} = ".format(k), ak)
        print("x_{} = ".format(k + 1), x)
        print("r_{} = ".format(k + 1), r)
        print("b_{} = ".format(k), bk)
        print("p_{} = ".format(k + 1), p)
        print("")
    return x

A = np.float64(np.array([[2,0,1],
         [0,5,0],
         [1,0,2]]))
b = np.float64(np.array([3,-5,3]))
x0 = np.float64(np.array([0,0,1/2]))

solution = conj_grad(A,b,x0,3)