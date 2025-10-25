#!/usr/bin/python3
"""
Script that returns states from the states table
"""

import MySQLdb
import sys

""" 0-select_states.py """
def get_all_states(username, password, dbname):
	""" List all states in the DB """
	try: 
		# Connect to server (Use with for auto closing and management)
		with MySQLdb.connect(
		    host="localhost",
		    port=3306,
		    user=username,
		    passwd=password,
		    db=dbname
		) as db:
			with db.cursor() as cursor:
				cursor.execute("SELECT * FROM states ORDER BY id ASC")
				for row in cursor.fetchall():
					print(row) 
	except MySQLdb.Error as err:
        print(f"Database error: {err}")
	
if __name__ == "__main__":
    get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
