# -*- coding: utf-8 -*-

# Dla drzewa BST napisać funkcje znajdujące największy i najmniejszy 
# element przechowywany w drzewie. Mamy łącze do korzenia, nie ma klasy 
# BinarySearchTree. Drzewo BST nie jest modyfikowane, a zwracana 
# jest znaleziona wartość. W przypadku pustego drzewa należy wyzwolić 
# wyjątek ValueError.

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass

def max_bst(node):
    if node is None:
        raise Exception("Empty tree")
    maxim = node.data
    if node.right:
        maxim = max(max_bst(node.right), maxim)
    if node.left:
        maxim = max(max_bst(node.left), maxim)
    return maxim


def min_bst(node):
    if node is None:
        raise Exception("Empty tree")
    minimal = node.data
    if node.right:
        minimal = min(min_bst(node.right), minimal)
    if node.left:
        minimal = min(min_bst(node.left), minimal)
    return minimal

node = Node(43)
node.insert(2)
node.insert(3423532)
node.insert(-4325)
node.insert(4)
node.insert(2)
node.insert(0)
node.insert(3)

print("Najmniejsza wartosc:")
print(min_bst(node))
print("Najwieksza wartosc:")
print(max_bst(node))

