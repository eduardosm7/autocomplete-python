from word import *


class Node:
    def __init__(self, item=None, value=None, left=None, mid=None, right=None):
        self.item = item
        self.value = value
        self.left = left
        self.mid = mid
        self.right = right


class TST:
    def __init__(self):
        self.root = Node()
        self.final_list = []

    def __insert(self, node, string, value):
        if len(string) == 0:
            return node
        head = string[0]
        tail = string[1:]
        if node is None:
            node = Node(head, None)
        if node.item is None:
            node.item = head
        if head < node.item:
            node.left = self.__insert(node.left, string, value)
        elif head > node.item:
            node.right = self.__insert(node.right, string, value)
        else:
            if len(tail) == 0:
                node.value = value
            else:
                node.mid = self.__insert(node.mid, tail, value)
        return node

    def insert(self, word):
        self.__insert(self.root, word.text, word.weight)

    # Adapted from https://gist.github.com/skylarker/f98c6c297ecc9a366836
    def __traverse(self, node):
        if node:
            for c in self.__traverse(node.left):
                yield c
            if node.value is not None:
                yield [node.item]
            else:
                for c in self.__traverse(node.mid):
                    yield [node.item] + c
            for c in self.__traverse(node.right):
                yield c

    def traverse(self):
        for w in self.__traverse(self.root):
            print(''.join(w))

    ######
    def search(self, prefix):
        pass

    def get_final_list(self):
        return self.final_list
