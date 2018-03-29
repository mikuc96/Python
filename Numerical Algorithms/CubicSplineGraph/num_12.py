from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1,1.03125,0.03125)
y =1/(1+5*x*x)
cs = CubicSpline(x, y,bc_type=((2, 0.0), (2, 0.0)))
x_new = np.linspace(-1.0, 1.0)
plt.plot(x_new,cs(x_new))
plt.show()
