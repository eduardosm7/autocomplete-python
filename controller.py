from palavra import *
from lista import List
#from trie import *
import time


class Controle:
        def __init__(self):
            self.number_of_items = 0
            self.items = list()
            self.data_loaded = None
            self.time = 0

        def __delete_items(self):
            self.items = []
            self.number_of_items = 0
            self.data_loaded = False

        def __first_index_of(self, prefix):
            begin = 0
            pos = -1
            return pos

        def __last_index_of(self, prefix):
            inicio = self.__first_index_of(prefix)
            return pos

        def load_list(self, filename):
            file = open(filename, 'r')
            raw_content = file.readlines()
            file.close()
            self.number_of_items = raw_content[0]
            for line in raw_content[1:]:
                tmp = line.strip("\n ").split("\t")
                item = Word(tmp[1], tmp[0])
                self.items.append(item)
            self.items.sort()
            self.data_loaded = True

        def find_list(self, prefix, q):
            pass
    
        def load_trie(self, filename):
            pass

        def find_trie(self, prefix, q):
            pass

        def get_time(self):
            pass
