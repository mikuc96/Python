# -*- coding: utf-8 -*-\

# Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy 
# liczby będące długościami jego boków.Jeżeli podane liczby nie 
# spełniają warunku trójkąta, to program ma generować wyjątek ValueError.

from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if not(abs(a-b)<a<b+c):
        raise ValueError("Uncorrect data!")
    p=0.5*(a+b+c)
    sol=sqrt(p*(p-a)*(p-b)*(p-c))
    return sol

print(heron(3,4,5))
print(heron(9,6,5))
print(heron(10,1,7)) # ValueError