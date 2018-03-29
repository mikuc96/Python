# -*- coding: utf-8 -*-
from random import random
from math import sqrt
from math import pi

# Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie 
# punktów z kwadratu z wpisanym kołem. Sprawdzić zależność dokładności 
# wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.

def calc_pi(n):
    '''Obliczanie liczby pi metod¹ Monte Carlo.
    n oznacza liczbê losowanych punktów.'''
    temp = 0.0
    l = []
    for i in range(1, n + 1):
        x = random()
        y = random()
        if (sqrt(x ** 2 + y ** 2) <= 1): temp = temp + 1.0
        l.append(float(4 * temp / i))
    return float(4 * temp / n), l

n=1000

for i in range(1, n + 1):
    sol=calc_pi(i)[0]
    error=pi-sol
    print("test: ",i, " ", sol,", error: ", abs(error))