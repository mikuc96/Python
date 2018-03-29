# -*- coding: utf-8 -*-

# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. 
# Zadbać o to, aby każda operacja była wykonywana w stałym czasie, 
# niezależnie od liczby elementów w kolejce.

from collections import deque
import random


class RandomQueue:

    def __init__(self):
        self.que = deque()

    def insert(self, data):
        self.que.append(data)
        self.que.rotate(random.randint(-len(self.que), len(self.que)))

    def remove(self):  # zwraca losowy element
        self.que.rotate(random.randint(-len(self.que), len(self.que)))
        return self.que.pop()

    def is_empty(self):
        return len(self.que) == 0

    def is_full(self):
        return False


que = RandomQueue()
for i in range(1000):
    que.insert(i)

print que.remove()
print que.remove()
print que.remove()
