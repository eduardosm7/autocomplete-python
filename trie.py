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

    def __insert(self, aux, word, counter=0):
        pass

    def insert(self, word):
        pass

    def __traverse(self, node, prefix, x="", y=0):
        pass

    def traverse(self, prefix):
        pass

    def search(self, prefix):
        pass

    def get_final_list(self):
        return self.final_list
