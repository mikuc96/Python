import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange as L

x=np.arange(-1,1.03125,0.03125)
b=1/(1+5*x*x)
x_new=np.linspace(-0.26,0.26)
log=L(x,b)

print (log)
for i in b:
    print (i)

plt.plot(x,b,'.')
plt.plot(x_new,log(x_new))
plt.show()

