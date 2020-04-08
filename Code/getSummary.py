'''
This file contains code to fetch the summary text based on book id from data.json
'''

import json

#reading the data.json for fetching summary text based on book id
with open("data.json", "r") as json_file:
	book_data = json.load(json_file)

summary_data = book_data["summaries"]

def getSummaryById(book_id):
	for summary in summary_data:
		if summary['id'] == int(book_id):
			return summary['summary']
	