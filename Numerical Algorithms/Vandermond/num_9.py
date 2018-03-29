import numpy as np
from numpy import power as p

n=5 #wymiar macierzy
x = np.array([-1.2300, -1.1900, -0.7400,  0.1100, 2.5600])
y = np.array([ 1.5129,  1.4161,  0.5476,  0.0121, 6.5536])

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


