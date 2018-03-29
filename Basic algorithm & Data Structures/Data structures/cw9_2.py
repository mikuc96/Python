# -*- coding: utf-8 -*-

# Mamy listy jednokierunkowe bez klasy SingleList. Napisać funkcję merge(), 
# która łączy dwie listy przez podłączenie drugiej na koniec pierwszej, 
# a zwraca nowy początek wspólnej listy. Uwzględnić możliwość pustych list.

import copy

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def printList(node):
    if node:
        print(node.data)
        printList(node.next)

def merge(node1, node2):
    if (node2 == None):
        return node1
    if (node1 == None):
        return node2
    temp = copy.copy(node1)
    while temp.next:
        temp = temp.next

    temp.next = node2
    return node1


list1 = None
list1 = Node(3, list1)
list1 = Node(2, list1)
list1 = Node(4, list1)

list2 = None
list2 = Node(5, list2)
list2 = Node(6, list2)
list2 = Node(7, list2)

print ("Lista pierwsza")
printList(list1)

print ("Lista druga")
printList(list2)

list3 = merge(list1, list2)
print ("Lista trzecia")
printList(list3)

del list1
del list2