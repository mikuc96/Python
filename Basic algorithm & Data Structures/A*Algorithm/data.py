#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graph import *

def graph1():
    graph=Graph()
    position_xy={"a":[2,2],
                "b":[5,4],
                "c":[8,3],
                "d":[9,5],
                "e":[14,6]}

    graph.add_edge("a", "b", 5)
    graph.add_edge("a", "c", 8)
    graph.add_edge("b", "c", 1)
    graph.add_edge("b", "d", 5)
    graph.add_edge("c", "d", 4)
    graph.add_edge("d", "e", 10)

    return graph, position_xy

def graph2():
    graph=Graph()
    position_xy={"a":[5,1],
                "b":[5,4],
                "c":[6,4],
                "d":[13,4],
                "e":[6,7],
                "f":[9,10],
                "g":[14,12],
                "h":[19,10]}

    graph.add_edge("a", "b", 2)
    graph.add_edge("a", "c", 4)
    graph.add_edge("b", "e", 1)
    graph.add_edge("c", "d", 2)
    graph.add_edge("c", "f", 8)
    graph.add_edge("e", "f", 3)
    graph.add_edge("f", "g", 3)
    graph.add_edge("f", "h", 10)
    graph.add_edge("g", "h", 2)

    return graph, position_xy

def graph3():
    graph=Graph()
    position_xy={"a":[3,3],
                "b":[14,4],
                "c":[6,7],
                "d":[10,13],
                "e":[16,11],
                "f":[20,6],
                "g":[24,11],
                "h":[22,16],
                "i":[20,11]}

    graph.add_edge("a", "g", 10)
    graph.add_edge("a", "c", 3)
    graph.add_edge("c", "b", 2)
    graph.add_edge("c", "d", 5)
    graph.add_edge("d", "h", 4)
    graph.add_edge("d", "e", 2)
    graph.add_edge("b", "e", 1)
    graph.add_edge("e", "f", 3)
    graph.add_edge("e", "i", 4)
    graph.add_edge("i", "g", 1)

    return graph, position_xy
