#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import *
from astar import *

g1, position_xy1=graph1()
g2, position_xy2=graph2()
g3, position_xy3=graph3()

path1, distance1=Astar(g1.get_graph(),position_xy1,'a','e')
path2, distance2=Astar(g2.get_graph(),position_xy2,'a','h')
path3, distance3=Astar(g2.get_graph(),position_xy2,'d','h')
path4, distance4=Astar(g3.get_graph(),position_xy3,'a','g')
path5, distance5=Astar(g3.get_graph(),position_xy3,'b','h')
path6, distance6=Astar(g3.get_graph(),position_xy3,'f','h')

print "////////////////////////////Graph1/////////////////////////////"
print_solution(path1,distance1,'a','e')
print position_xy1

print "////////////////////////////Graph2/////////////////////////////"
print_solution(path2,distance2,'a','h')
print_solution(path3,distance3,'d','h')

print "////////////////////////////Graph3/////////////////////////////"
print_solution(path4,distance4,'a','g')
print_solution(path5,distance5,'b','h')
print_solution(path6,distance6,'f','h')