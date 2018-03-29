# -*- coding: utf-8 -*-

from cw7_Point import Point
from math import pi, sqrt

# W pliku circles.py zdefiniować klasę Circle wraz z potrzebnymi metodami. 
# Okrąg jest określony przez podanie środka i promienia. 
# Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł circles.

class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if (not isinstance(x, float or int) and isinstance(y, float or int) and isinstance(radius, float or int)):
            raise ValueError("incorrect type of data")
        if radius < 0:
            raise ValueError("negative radius")
        self.pt = Point(x, y)
        self.radius = float(radius)

    def __repr__(self):  # "Circle(x, y, radius)"
        return "Circle(%i, %i, %i)" % (self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("incorrect type of data")
        return self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return pi * self.radius * self.radius

    def move(self, x, y):  # przesuniecie o (x, y)
        if not (isinstance(x, float) or isinstance(x, int)) and (isinstance(y, float) or isinstance(y, int)):
            raise ValueError("incorrect type of data")
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):  # okrąg pokrywający oba
        if not isinstance(other, Circle):
            raise ValueError("incorrect type of data")
        X = ((self.pt.x + other.pt.x + self.radius + other.radius) / 2)
        Y = ((self.pt.y + other.pt.y + self.radius + other.radius) / 2)
        R = (sqrt(X * X + Y * Y))
        return Circle(X, Y, R)


import unittest
class Test_circle(unittest.TestCase):
    def setUp(self):
        self.r1 = Circle(1, 1, 1)
        self.r2 = Circle(5, 1, 1)

    def test_print(self):
        self.assertEqual(repr(self.r1), "Circle(1, 1, 1)")
        self.assertEqual(repr(self.r2), "Circle(5, 1, 1)")

    def test_equal(self):
        self.assertTrue(self.r1 == self.r1)

    def test_area(self):
        self.assertTrue(self.r1.area() == pi)

    def test_move(self):
        self.assertEqual(self.r1.move(0, 0), self.r1)
        self.assertEqual(self.r2.move(0, 0), self.r2)
        self.assertEqual(self.r1.move(-2, -5), Circle(-1, -4, 1))
        self.assertEqual(self.r2.move(4, -10), Circle(9, -9, 1))

    def test_cover(self):
        self.assertTrue(Circle.cover(self.r1, self.r2) != Circle(4, 2, 4))


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
