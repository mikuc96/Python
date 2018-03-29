#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1. 
# Następnie program wylosuje liczbę y z tego samego zakresu i znajdzie wszystkie jej 
# wystąpienia na liście L przy pomocy wyszukiwania liniowego. [n=100, k=10]

import random

def create_list(n, k):
    L = []
    for i in range(n):
        L.append(random.randint(0, k - 1))
    return L

def linear_search(L, left, right, y):
    i = left
    while i <= right:
        if y == L[i]:
            return i
        i += 1
    return None

i,n,k=0,100,10
l = create_list(n, k); size_l=len(l)
random_int=random.randint(0, k-1)
print "Random list: ",l
print "Random int: ",random_int

while i<=size_l-1:
    if i==None: break
    else: i += 1; i= linear_search(l, i, size_l - 1, random_int); print i



