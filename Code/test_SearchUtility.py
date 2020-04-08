import unittest
from SearchUtility import *
from TrieInsertAll import InsertData

class TestSearchQuery(unittest.TestCase):
	def test_insert(self):
		#checking inserting data to Trie
		self.assertTrue(InsertData("sampleData.json"))

	def test_returned_res(self):
		#test if returned results are right
		self.assertEqual(len(searchBook("Practicing meditation", 2)), 1)
		self.assertEqual(len(searchBook("that", 2)), 2)
		self.assertEqual(len(searchBook("RAMDOMSTRINGCHECK", 4)), 0)
