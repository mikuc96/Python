#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import PriorityQueue

def h(node1, node2):
    """funkcja do określania odległości w lini prostej, nasza heurystyka"""
    x1,y1=node1
    x2,y2=node2
    return abs(x1 - x2) + abs(y1 - y2)

def Astar(graph, position_xy, start, end):
    """Głowna funkcja zwracająca ścieżkę przejść między start->end oraz odległość między nimi"""

    queue = PriorityQueue()
    queue.put(start, 0)
    visited = {}
    visited[start] = None
    distance_from_start = {}
    distance_from_start[start] = 0

    while queue:
        temp = queue.get()
        if temp == end: break
        for node in graph[temp]:
            g = distance_from_start[temp] + graph[temp][node]
            if node not in distance_from_start or g < distance_from_start[node]:
                distance_from_start[node] = g
                f = g + h(position_xy[end], position_xy[node])
                queue.put(node, f)
                visited[node] = temp

    path=build_proper_path(visited, start, end)
    distance=distance_from_start[end]
    return path, distance

def build_proper_path(visited, start, end):
    """Pomocnicza funkcja która odbudowywuje ściezkę na podstawie danych visited """
    temp = end
    path = []
    while temp != start:
        path.append(temp)
        temp = visited[temp]
    path.append(start)
    path.reverse()
    return path

def print_solution(path, distance,start,end):
    """Metoda odpowiedzialna za fomrmatowanie danych i wyświetlanie je"""
    print "Path",start,"->",end,"=",path,"Distance =", distance
