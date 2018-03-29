# -*- coding: utf-8 -*-

# Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu. 
# Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku 
# przepełnienia stosu. Napisać kod testujący stos.

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if (self.n == self.size):
            raise ValueError('Stack is full')
        self.items[self.n] = data
        self.n += 1

    def pop(self):

        if(self.n==0):
            raise ValueError('Stack is empty')
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data



import unittest
class Test(unittest.TestCase):

    def test_stack_normal(self):
        stack = Stack()
        stack.push(7)
        stack.push(3)
        stack.push(5)
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 7)

    def test_pop(self):
        stack = Stack()
        stack.pop()

    def test_push(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

if __name__ == "__main__":
    unittest.main()  # wszystkie testy