#!/usr/bin/python3
"""
Script that lists all states starting with N
"""

import MySQLdb
import sys


def get_states_starting_with_N(username, password, dbname):
	try:
		with MySQLdb.connect(
			host="localhost",
			port=3306,
			user=username,
			passwd=password,
			db=dbname
		) as db:
			with db.cursor() as cursor:
				cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
				for row in cursor.fetchall():
					print(row)
	except MySQLdb.Error as e:
		print(f'Database error: {e}')


if name == "__main__":
	get_states_starting_with_N(sys.argv[1], sys.argv[2], sys.argv[3])
