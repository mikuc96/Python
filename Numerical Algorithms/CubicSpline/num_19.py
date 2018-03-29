import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

tab=np.loadtxt('dane.txt')
tab=np.array(tab)
size=np.size(tab)

args=[]
vals=[]

for i in range(0,512):
    args.append(tab[i,0])
    vals.append(tab[i,1])


cs = CubicSpline(args, vals,bc_type=((2, 0.0), (2, 0.0)))

x_new = np.linspace(-2, 2)
plt.plot(x_new,cs(x_new))
plt.show()