'''
This file contain code to search strings in the Trie and return to actual flask endpoint to the user
'''

#importing all the required modules
import pickle, json
import http.client
from getSummary import *
from collections import Counter

#reading Trie object from the disk
filehandler = open("TrieObject", 'rb') 
t = pickle.load(filehandler)

#making connection to api to get book author name
conn = http.client.HTTPSConnection("ie4djxzt8j.execute-api.eu-west-1.amazonaws.com")

#function to get all details based on search query
#param: queries - string to search, k - number of result to return
def searchBook(queries, k):
	#this list will hold all the book id that we have search query
	id_lists = []
	search_q = queries
	for i in search_q.split():
		#searching in the Trie. if matched, this will return the book id otherwise -1
		found_id = t.search(i)
		if found_id != -1:
			id_lists.extend(found_id)

	#finding the most book id with the matching based on user query
	c = Counter(id_lists)
	most_common = [key for key, val in c.most_common(int(k))]
	
	final_res = []

	#now looping through relavent book id to get the author data from the API
	for i in most_common:
		payload = "{\"book_id\": "+str(i)+"\n}"

		headers = {
		    'content-type': "application/json"
		}

		conn.request("POST", "/coding", payload, headers)

		res = conn.getresponse()
		data = res.read().decode("utf-8")
		data = data[12:][:-2]

		res = {}
		res['id'] = i
		res['queries'] = queries.replace("\"","")
		res['author'] = data
		res['summary'] = getSummaryById(str(i)) #getting summary for a book id
		final_res.append(res)

	return final_res
