# -*- coding: utf-8 -*-

# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych: 
# (a) różne liczby int od 0 do N-1 w kolejności losowej, 
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji), 
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności, 
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim, 
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).

import random, math

def normalRandom(N):
    temp = list(range(N))
    random.shuffle(temp)
    return temp

def nearlyRandom(N):
    l = list(range(N))
    for i in range(int(N / 5)):
        x = int(random.uniform(0, N - 1))
        y = int(random.uniform(0, N - 1))
        temp = l[y]
        l[y] = l[x]
        l[x] = temp
    return l

def reversedNearlyRandom(N):
    l = nearlyRandom(N)
    l.reverse()
    return l

def gaussRandom(N):
    return [round(random.gauss(96, 25)) for x in range(N)]


def colectionRandom(N):
    return [random.randint(0, math.floor(math.sqrt(N))) for x in range(N)]

n=25
print normalRandom(n)
print nearlyRandom(n)
print reversedNearlyRandom(n)
print gaussRandom(n)
print colectionRandom(n)
