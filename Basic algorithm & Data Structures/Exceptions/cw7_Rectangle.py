#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. 
# Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł rectangles.

import math as M
from cw7_Point import Point
class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if not(x1 <= x2 and y1 <= y2): raise ValueError("incorrect data")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[%s, %s]" % (self.pt1, self.pt2)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle" + "[%s, %s]" % (self.pt1, self.pt2)

    def __eq__(self, other):  # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            raise ValueError("incorrect type of data")
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        else:
            return False

    def __ne__(self, other):  # obsługa rect1 != rect2
        if not isinstance(other, Rectangle):
            raise ValueError("incorrect type of data")
        if self.__eq__(other):
            return False
        else:
            return True

    def center(self):  # zwraca środek prostokąta
        point = Point()
        point.x = self.pt2.x - (self.pt2.x - self.pt1.x) / 2
        point.y = self.pt2.y - (self.pt2.y - self.pt1.y) / 2
        return point

    def area(self):  # pole powierzchni
        a = abs(self.pt2.x - self.pt1.x)
        b = abs(self.pt2.y - self.pt1.y)
        return a * b

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)


import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
	self.r1 = Rectangle(1., 1., 4., 4.)
	self.r2 = Rectangle(1., 3., 5., 8.)
	self.r3 = Rectangle(1., 1., 4., 4.)


    def test_print(self):
        self.assertEqual(str(self.r1), "[(1.0, 1.0), (4.0, 4.0)]")
        self.assertEqual(repr(self.r1), "Rectangle[(1.0, 1.0), (4.0, 4.0)]")

    def test_equal(self):
        self.assertEqual(self.r1 == self.r2, False)
        self.assertEqual(self.r1 == self.r3, True)
        self.assertEqual(self.r1 != self.r2, True)
        self.assertEqual(self.r1 != self.r2, True)

    def test_center(self):
        self.assertEqual(str(self.r1.center()), '(2.5, 2.5)')

    def test_area(self):
        self.assertEqual(self.r1.area(), 9)

    def test_move(self):
        self.assertEqual(str(self.r1.move(1, 1)), '[(2.0, 2.0), (5.0, 5.0)]')


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
