# -*- coding: utf-8 -*-

# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). 
# orównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) 
# do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.

import time


def P(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i == 0:
        return 1.0
    elif j == 0:
        return 0.0
    else:
        return 0.5 * (P(i - 1, j) + P(i, j - 1))



data = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}
def P_dynamic(i, j):
    if i == 0:
        return 1.0
    elif j == 0:
        return 0.0
    else:
        v = data.get((i, j))
        if (v != None):
            return v
        else:
            v = 0.5 * (P_dynamic(i - 1, j) + P_dynamic(i, j - 1))
            data[(i, j)] = v
            return v

def Test(i, j):
    time_P_start=time.clock()
    solve_p=P(i,j)
    time_P_stop=time.clock()
    time_P=time_P_stop-time_P_start

    time_P_dynamic_start=time.clock()
    solve_p_dynamic=P_dynamic(i,j)
    time_P_dynamic_stop=time.clock()
    time_P_dynamic=time_P_dynamic_stop-time_P_dynamic_start
    time_difference=time_P-time_P_dynamic

    return("Solve P(): %s,  Time:%s  || Solve P_dynamic():%s  Time:%s Time_diffrence:%s" % (solve_p, time_P, solve_p_dynamic, time_P_dynamic,time_difference))

print(Test(10,8))
print(Test(1,10))
print(Test(0,0))
print(Test(4,20))
print(Test(4,60))
print(Test(4,70))
print(Test(3,90))
print(Test(4,120))

