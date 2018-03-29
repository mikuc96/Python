import math as m
import numpy as np


def f(x):
    return m.sin(m.pi*(1.0+m.sqrt(x))/(1.0+x*x))

def trap(x,y,z):
    return (m.pow(4.0, x+1.0)*y-z)/(m.pow(4.0, x+1.0)-1.0)

def romber(i,a,b):

    q=(b-a)/(m.pow(2.0,i))
    wynik=0.0
    k=0;
    l=(m.pow(2.0, i)-1.0)
    l=int(l)
    for k in range(0,l):
        wynik=wynik+ (f(a+(k*q))+f(a+(k+1))*q) / 2.0
    wynik=q*wynik
    k+=1
    return wynik


a=0.0; b=17.0

k=0
i=0
last=1
while(i<20):
    tab_nowy=np.zeros(i+1)
    if(i==0):
        tab_nowy[i]=romber(1,a,b)
    else:
        for k in range(0,10):
            if(k==0):
                tab_nowy[0]=romber(i,a,b)
            else:
                tab_nowy[k]=trap(k-1,tab_nowy[k-1],tab_poprzedni[k-1])
        if (i>2) and ((tab_nowy[i-1]-last)<tol) and ((tab_nowy[i-1]-last)>-tol):
            print(tab_nowy[i-1])
            break
        last=tab_nowy[i-1]
        tab_poprzedni=tab_nowy.copy()
        i+=1

    print(tab_nowy[i])



