#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Napisać wersję rekurencyjną wyszukiwania binarnego.

import random
def binarySearch(L, left, right, y):
    def recurse(first, last):
        mid = (first + last) / 2 
        if first > last:
            return False
        elif (L[mid] < y):
            return recurse(mid + 1, last)
        elif (L[mid] > y):
            return recurse(first, mid - 1)
        else:
            return True

    return recurse(left, right)
    
l1 = [random.randint(0,1000) for i in range(10)]; l1.sort()
l2 = [random.randint(0,1000) for i in range(20)]; l2.sort()
print l1,l1[3],'\n',l2,l2[14]

print(binarySearch(l1, 0, len(l1)-1, l1[3]))
print(binarySearch(l2, 0, len(l2)-1, l2[14]))
print(binarySearch(l2, 0, len(l2)-1, l2[14]-1))#in most cases return false