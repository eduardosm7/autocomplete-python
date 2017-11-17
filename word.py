class Word:

    def __init__(self, text="", weight=-1):
        self.text = text
        self.weight = weight

    def __lt__(self, other):
        return self.text < other.text
    
    def __str__(self):
        return "{0}, {1}".format(self.text, self.weight)
    
    def __repr__(self):
        return self.__str__()


def compare_by_prefix(word, prefix):
    word.text = word.text.lower()
    prefix = prefix.lower()
    prefix_size = len(prefix)
    if prefix < word.text[:prefix_size]:
        return 1
    if prefix > word.text[:prefix_size]:
        return -1
    return 0


def compare_by_weight(word1, word2):
    if word1.weight > word2.weight:
        return 1
    if word1.weight < word2.weight:
        return -1
    return 0
