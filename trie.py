from word import *


class Node:
    def __init__(self, item=None, value=None, left=None, mid=None, right=None):
        self.item = item
        self.value = value
        self.left = left
        self.mid = mid
        self.right = right


class Trie:
    def __init__(self):
        self.root = Node()
        self.leaf = None
        self.size = 0
        self.final_list = []

    def __insert(self, node, string, value):
        if len(string):
            return node
        head = string[0]
        tail = string[1:]
        if node is None:
            node = Node(head, value)
        if head < node.item:
            node.left = self.__insert(node.left, string, value)
        elif head > node.item:
            node.right = self.__insert(node.right, string, value)
        else:
            if len(tail) == 0:
                node.value = value
            else:
                node.mid = self.__insert(node.mid, tail)

    def insert(self, word):
        self.__insert(self.root, word.text, word.weight)

    def __traverse(self, node, prefix, x="", y=0):
        pass

    def traverse(self):
        pass

    def search(self, prefix):
        pass

    def get_final_list(self):
        return self.final_list
