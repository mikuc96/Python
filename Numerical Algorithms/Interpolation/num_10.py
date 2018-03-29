import numpy as np
from numpy import power as p
import matplotlib.pyplot as plt

n=8 #wymiar macierzy
x = np.array([0.062500,0.187500,0.312500,0.437500,0.562500,0.687500,0.812500,0.935700])
y = np.array([0.687959,0.073443,-0.517558,-1.077264,-1.600455,-2.080815,-2.507266,-2.860307])

x_new=np.linspace(-1, 1)

size=x.size
Vandermond=np.zeros((size,size))
b=y.copy()

for i in range(0,n):
    for j in range(0,n):
        Vandermond[i,j]=p(x[i],n-1-j)

solves=np.linalg.solve(Vandermond,b)
print("Solves:")
for i in solves:
    print(i)

polynomial=0
for i in range(0,n):
    polynomial+=solves[i]*p(x_new,n-1-i)

plt.plot(x,y,'o',color='#000000')
plt.plot(x_new,polynomial)
plt.show()
