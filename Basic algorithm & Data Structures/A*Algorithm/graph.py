#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:
    """Klasa reprezentująca postać grafu nieskierowanego"""

    def __init__(self):
        self.graph = {}


    def add_node(self, node):
        """Dodaje wierzchołek do grafu nieskierowanego."""
        if node not in self.graph:
            self.graph[node] = {}


    def add_edge(self, start, stop, weight):
        """Dodaje krawędź do grafu nieskierowanego."""
        self.add_node(start)
        self.add_node(stop)

        if stop not in self.graph[start]:
            self.graph[start][stop] = weight
            self.graph[stop][start] = weight  # undirected graph


    def get_nodes(self):
        """Zwraca listę wierzchołków."""
        return self.graph.keys()


    def get_edges(self):
        """Zwraca listę krawędzi."""
        L = []
        for item in self.graph:
            for node in self.graph[item]:
                L.append((item, node, self.graph[item][node]))
        return L


    def get_graph(self):
        """Zwraca instancję grafu w postaci słownikowej."""
        return self.graph


    def print_graph(self):
        """Metoda pomocnicza służąca do wyświetlania grafu
           w postaci teksowej."""

        for start in self.graph:
            print start, ":",
            for stop in self.graph[start]:
                print "%s(%s)" % (stop, self.graph[start][stop]),
            print
