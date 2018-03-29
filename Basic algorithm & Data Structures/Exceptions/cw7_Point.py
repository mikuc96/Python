#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import math as M

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point" + "(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        if self.x == other.x and other.y == self.y:
            return True
        else:
            return False

    def __ne__(self, other):  # obsługa point1 != point2
        if self.x == other.x and other.y == self.y:
            return False
        else:
            return True

    def __add__(self, other):  # v1 + v2
        sum = Point()
        sum.x = self.x + other.x
        sum.y = self.y + other.y
        return sum

    def __sub__(self, other):  # v1 - v2
        sub = Point()
        sub.x = self.x - other.x
        sub.y = self.y - other.y
        return sub

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        l = self.x * self.x + self.y * self.y
        return M.sqrt(l)


# Kod testujący moduł.

import unittest
class TestPoint(unittest.TestCase):

    def setUp(self):
        self.other = Point(2, 3)
        self.point = Point(4, 5)

    def test_str(self):
        self.assertEqual(str(self.point), "(4, 5)")

    def test_repr(self):
        self.assertEqual(repr(self.point), "Point(4, 5)")

    def test_eq(self):
        self.assertEqual(self.point==self.other, False)

    def test_ne(self):
        self.assertEqual(self.point!=self.other, True)

    def test_add(self):
        self.assertEqual(str(self.point+self.other), "(6, 8)")

    def test_sub(self):
        self.assertEqual(str(self.point-self.other), "(2, 2)")

    def test_mul(self):
        self.assertEqual(str(self.point*self.other),'23')

    def test_cross(self):
        self.assertEqual(self.point.cross(self.other), 2)

    def test_length(self):
        self.assertEqual(self.point.length(),6.4031242374328485)

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testyss
