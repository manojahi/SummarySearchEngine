'''
Flask app which will be exposed to end user for searching for the books
'''

from flask import Flask, request
import json
from SearchUtility import *

application = Flask(__name__)
application.secret_key = 'development key'

@application.route("/search", methods=["GET", "POST"])
def SearchBook():
	#getting search queries in format - query1;query2;query2;....
	queries_list = request.values.get('queries').split(';')
	k = request.values.get('k')

	final_return = []
	for queries in queries_list:
		#calling the search utility
		returned_list = searchBook(queries, k)				
		final_return.append(returned_list)

	#return final searched json to user
	return json.dumps(final_return)

if __name__ == "__main__":
	application.run(debug=True)
