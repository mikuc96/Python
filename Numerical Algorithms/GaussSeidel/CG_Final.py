import numpy as np
from scipy.sparse.linalg import cg
import tensorflow as tf
import time
from scipy.sparse import dia_matrix
import math as m
import matplotlib.pyplot as plt
import sys as s
from scipy.interpolate import PchipInterpolator as Pch
norm= np.zeros(25)
def conjugate_grad(A, b):
    n=len(b)
    x = np.zeros(n)
    r = b-A.dot(x)
    w = - r
    z=A.dot(w)
    a = r.dot(w)/w.dot(z)
    x = x + (a * w)
    x_prev=np.zeros(n)

    for i in range(25):
        r=r-a*z

        B=(r.dot(z))/(w.dot(z))
        w=-r+(B*w)
        z=A.dot(w)
        a=(r.dot(w))/(w.dot(z))
        x=x+(a*w)
        norm[i]=np.linalg.norm(x-x_prev)
        x_prev=x.copy()
    print(norm)
    return x
n=128
A=dia_matrix(np.diag([1.0]*(n-4),-4)+np.diag([1.0]*(n-1),-1)+np.diag([4.0]*n,0)+np.diag([1.0]*(n-1),1)+np.diag([1.0]*(n-4),4))
b=np.ones(n)
x=conjugate_grad(A,b)
for i in range(x.size):
    s.stdout.write("x%d="%(i+1))
    print("%.5f" % x[i])

arg=np.arange(0,25,1)

cs=Pch(arg,norm)
arg_new=np.linspace(0,25,100)
plt.plot(arg,norm,'o')
plt.plot(arg_new,cs(arg_new))
plt.show()