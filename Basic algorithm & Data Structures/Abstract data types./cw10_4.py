# -*- coding: utf-8 -*-

# Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. 
# Poprawić metodę put() w tablicowej implementacji kolejki, 
# aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.

class Queue:

    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if (self.is_full()):
            raise ValueError("Queue is full")
        self.items[self.tail] = data
        self.tail = (self.tail + 1)

    def get(self):
        if (self.is_empty()):
            raise ValueError("Queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None  # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest
class Test(unittest.TestCase):

    def test(self):
        que = Queue()
        que.put(1)
        que.put(1)
        que.put(1)
        que.get()
        que.get()
        que.get()

    def test1(self):
        que1 = Queue()
        que1.put(1)
        que1.put(1)
        que1.put(1)
        que1.put(1)
        que1.put(1)
        que1.put(1)

    def test2(self):
        que2 = Queue()
        que2.get()

if __name__ == "__main__":
    unittest.main()  # wszystkie testy
