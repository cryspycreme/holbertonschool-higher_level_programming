#!/usr/bin/python3
"""
Script that returns states form the states table
"""
import MySQLdb
import sys


def get_states(username, password, dbname):
    """ Get all states from states db table starting with N"""
    try:
        # Connect to server (Use with for auto closing and management)
        with MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=dbname) as db:

            with db.cursor() as cur:
                cur.execute("SELECT * FROM states WHERE name"
                            " LIKE BINARY 'N%' ORDER BY id ASC")
                # Fetch and display results
                results = cur.fetchall()
                for row in results:
                    print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3])
