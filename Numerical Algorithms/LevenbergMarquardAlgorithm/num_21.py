import numpy as np
import numdifftools as nd
from numpy.linalg import inv
import matplotlib.pyplot as plt

def LeMa(x):
    f=lambda  x:100*(x[1]- x[0]**2)**2 + (1 - x[0])**2
    l=1/1024
    def Grad(x):
        g = nd.Gradient(f)
        h=g(x)
        return h

    def Hes(x):
        h=nd.Hessian(f)
        h=h(x)
        h[0, 0] = (1 + l) * h[0, 0]
        h[1, 1] = (1 + l) * h[1, 1]
        return h


    x_test = x - (inv(Hes(x)).dot(Grad(x)))
    iter=100
    solutions=np.zeros((iter,2))
    for i in range(iter):
        grad=Grad(x)

        if(f(x_test)>f(x)):
            l=l*10
            x_test = x - (inv(Hes(x)).dot(grad))

        if (f(x_test) < f(x)):
            l=l/10
            x=x_test.copy()
            x_test = x - (inv(Hes(x)).dot(Grad(x)))
        solutions[i]=x

    args=np.arange(0,iter,1)
    plt.plot(args,solutions,'r')
    plt.show()

point1=np.array([-3,-4])
point2=np.array([6,0])
point3=np.array([-6,4])
point4=np.array([6,6])
point5=np.array([-10,8])

LeMa(point1)
LeMa(point2)
LeMa(point3)
LeMa(point4)
LeMa(point5)
