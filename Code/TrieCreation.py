'''
This file contains all the code related to creation of Trie. Inserting data to trie and searching for strings in trie
'''

from collections import defaultdict 

#class defining the Trie node with all the relevent info
class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.end = False
        self.book_id = [] #list to store book id with each node

#class for creating a tree and other methods such as inserting, searching
class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word, book_id):

        root = self.root
        length = len(word)

        try:
            for i in range(length):
                index = self.get_index(word[i])

                if index not in root.children:
                    root.children[index] = self.get_node()
                root = root.children.get(index)

            root.end = True
            root.book_id.append(book_id)
        except:
            raise Exception('Error while inserting to Trie')


    def search(self, word):
        root = self.root
        length = len(word)

        for i in range(length):
            index = self.get_index(word[i])
            if not root:
                return -1
            root = root.children.get(index)

        return root.book_id if root and root.end else -1
