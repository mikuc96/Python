import numpy as np
import sys as s
import math as m
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

n=128
A=np.diag([1.0]*(n-4),-4)+np.diag([1.0]*(n-1),-1)+np.diag([4.0]*n,0)+np.diag([1.0]*(n-1),1)+np.diag([1.0]*(n-4),4)
b=np.ones(n)
x = np.zeros(n)
x_prev = np.zeros(n)
p=25
fx_p=np.zeros(p)

for k in range(0,p):
    for i in range(0,n):
        s1 = 0.
        s2 = 0.
        if(i==0):
            s2=(A[i,i+1]*x_prev[i+1])+(A[i,i+4]*x_prev[i+4])
        elif(i>0 and i<4):
            s1=A[i,i-1]*x[i-1]
            s2 = (A[i, i + 1] * x_prev[i + 1]) + (A[i, i + 4] * x_prev[i + 4])
        elif(i>=4 and i<n-4):
            s1=A[i,i-4]*x[i-4]+A[i,i-1]*x[i-1]
            s2 = (A[i, i + 1] * x_prev[i + 1]) + (A[i, i + 4] * x_prev[i + 4])
        elif(i>=n-4 and i<(n-1)):
            s1 = A[i, i - 4] * x[i - 4] + A[i, i - 1] * x[i - 1]
            s2 = A[i, i + 1] * x_prev[i + 1]
        elif(i==(n-1)):
            s1 = A[i, i - 4] * x[i - 4] + A[i, i - 1] * x[i - 1]
        x[i]=(b[i]-s1-s2)/A[i,i]
    norm=0
    norm=np.linalg.norm(x-x_prev)
    fx_p[k]=norm
    x_prev=x.copy()


for i in range(x.size):
    s.stdout.write("x%d="%(i+1))
    print("%.5f" % x[i])

arg=np.arange(0,p,1)

cs=CubicSpline(arg,fx_p)
arg_new=np.linspace(0,p,100)

plt.plot(arg,fx_p,'o')
plt.plot(arg_new,cs(arg_new))
plt.show()
