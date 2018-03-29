from numpy.polynomial.laguerre import lagroots, lagfromroots
import numpy as n


def print_roots(p,roots):
    print(p)
    size=roots.size
    for i in range(size):
        print(roots[i])
    print()

p=n.poly1d([243,-486,783,-990,558,-28,-72,16])
p_roots=lagroots(p)


print_roots(p,p_roots)

p2=n.poly1d([1,1,3,2,-1,-3,-11,-8,-12,-4,-4])
p_roots2=lagroots(p2)

print_roots(p2,p_roots2)

p3=n.poly1d([1,complex(0,1),-1,complex(0,-1),1])
p_roots3=lagroots(p3)
print_roots(p3,p_roots3)