#UniBuddy Assignment submitted by Manoj Ahirwar

Steps to follow to run the code:
1. First we need to insert data.json to Trie by running following command (we need to pass json filename as arg to script)
	- python TrieInsertAll.py data.json
2. Now run Flask app by
	- python application.py
	  : This will run flask application on http://127.0.0.1:5000/

3. Now to test the api.
	- POST Request on: http://127.0.0.1:5000/search
	- POST Args: 
	queries: is your problems;achieve take book
	k: 3
	- API post call: http://127.0.0.1:5000/search?queries=is your problems;achieve take book&k=2


*Files*
TrieCreation.py - This file contains all the code related to creation of Trie. Inserting data to trie and searching for strings in trie
TrieInsertAll.py - This file contains code to reading all the data and inserting it into Trie and saving final Trie object to disk for later usage
SearchUtility.py - This file contain code to search strings in the Trie and return to actual flask endpoint to the user
getSummary.py - This file contains code to fetch the summary text based on book id from data.json
application.py - Flask app which will be exposed to end user for searching for the books
test_SearchUtility.py - file containing testcases
sampleData.json - summary data for testcase purpose
data.json - actual data for the application