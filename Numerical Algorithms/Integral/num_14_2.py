import math as m
import numpy as n
from scipy.integrate import romberg
from scipy.special import erf
import matplotlib.pyplot as plt
def f(x):
    return m.sin(m.pi*(1.0+m.pow(x,1/2))/(1.0+x*x))*m.pow(m.e,-x)

solution=romberg(f,0,1,show=True)
solution2=romberg(f,1,10,show=True)
print(n.linalg.norm(solution)+n.linalg.norm(solution2))
x = n.arange(0.0, 100, 0.1)
f2 = n.vectorize(f)
plt.plot(x,f2(x),'-r')
plt.show()