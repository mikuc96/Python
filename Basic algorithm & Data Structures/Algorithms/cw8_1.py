# -*- coding: utf-8 -*-

# Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0. 
# Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, 
# schematu blokowego, drzewa. Podać implementację algorytmu 
# w Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("Równanie jest nieokreślone.")
        else:
            print("Równanie sprzeczne.")
    elif a == 0:
        print("Rozwiązaniem jest prosta: y = " + repr(-float(c) / float(b)))
        return
    elif b == 0:
        print("x = " + repr(-float(c) / float(a)))
    else:
        print("y = " + str(float(-c) / float(b)) + "+(" + str(float(-a) / float(b)) + ")x")


solve1(2, 1, -9)
solve1(0, 0, 0)
solve1(0, 0, 1)
solve1(5, 0, 3)


