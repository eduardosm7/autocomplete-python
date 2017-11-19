from word import *
from chained_list import List
#from trie import *
import time


class Controller:
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
            for item in self.items:
                if compare_by_prefix(item, prefix) == 0:
                    pos = begin
                    break
                begin += 1
            return pos

        def __last_index_of(self, prefix):
            start = self.__first_index_of(prefix)
            pos = start
            if start != -1:
                for item in self.items[start+1:]:
                    if compare_by_prefix(item, prefix) == 1:
                        break
                    pos += 1
            return pos

        def load_items(self, filename):
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

        def find_list(self, prefix, quantity):
            begin = self.__first_index_of(prefix)
            end = self.__last_index_of(prefix)
            chained_list = List()
            for word in self.items[begin:end+1]:
                chained_list.insert_ordered(word, compare_by_weight, True)
            for i in range(chained_list.get_size()-quantity):
                chained_list.remove_end()
            return chained_list

        def find_trie(self, prefix, quantity):
            pass

        def get_time(self):
            pass
