import numpy as n
import math as m
import matplotlib.pyplot as plt
from scipy.integrate import romberg

def f(x):
    return m.cos((1+x)/((x*x)+0.04))*m.pow(m.e,-(x*x))

x=n.arange(-5,5,0.01)
y=n.zeros(x.size)
for i in range(x.size):
    y[i]=romberg(f,-10,x[i],divmax=50)

limit=y[y.size-1]
print(limit)
plt.plot(x,y,'r')
plt.show()