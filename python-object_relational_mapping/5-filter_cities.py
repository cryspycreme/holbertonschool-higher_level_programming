#!/usr/bin/python3
"""
Module 5 - All cities by state
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, dbname, state_name):
    """
    Connec to db and run script to
    list cities by state
    """
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=dbname
                )
        cursor = db.cursor()
        query = """"
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name))
        results = cursor.fetchall()
        for cities in results:
            print(cities)
    except MySQLdb.Error as e:
        print(f'Database error: {e}')
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
