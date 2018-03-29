# -*- coding: utf-8 -*-

# heapSort jest algorytmem sortującym ktory wykorzystuje wlasności kopca binarnego zaimplementowanego
# przy pomocy tablicy. Pierwsza faza algorytmu polega na zbudowaniu kopca a druga na wlasciwym sortowaniu.
# Algorytm pracuje z szybkościa O(nlogn) oraz ze stała złozonoscia pamieciowa O(n). Algorytm ten jest z reguły
# wolniejszy od quicksort natomiast ma lepsza złożoność pesymistyczną O(nlogn), quicksort(n**2)

def heapSort(l):
    size = len(l) - 1
    n = size / 2
    for i in range(n, -1, -1):
        moveDown(l, i, size)

    for i in range(size, 0, -1):
        if l[0] > l[i]:
            swap(l, 0, i)
            moveDown(l, 0, i - 1)


def moveDown(l, first, last):
    largest = 2 * first + 1
    while largest <= last:

        if (largest < last) and (l[largest] < l[largest + 1]):  largest += 1

        if l[largest] > l[first]:
            swap(l, largest, first)
            first = largest;
            largest = 2 * first + 1
        else:
            return


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heapSort(l)
print(l)
