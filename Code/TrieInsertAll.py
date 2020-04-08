'''
This file contains code to reading all the data and inserting it into Trie and saving final Trie object to disk for later usage
'''

#importing all required modules
from TrieCreation import *
import json
import pickle
import sys

def InsertData(filename):
    try:
        #reading the data.json
        with open(filename, "r") as json_file:
            book_data = json.load(json_file)

        summary_data = book_data["summaries"]

        #Initialization of Trie object
        t = Trie()

        for summary in summary_data:
            for word in summary["summary"].split():
                #adding all the words to the Trie
                t.insert(word, summary["id"])        

        #Saving created Trie to disk for later usage
        filehandler = open("TrieObject", 'wb') 
        pickle.dump(t, filehandler)
        return True
    except:
        return False

if __name__ == "__main__":
    filename = sys.argv[1]
    InsertData(filename)