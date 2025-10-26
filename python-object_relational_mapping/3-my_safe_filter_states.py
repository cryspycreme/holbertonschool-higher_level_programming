#!/usr/bin/python3
"""
Script that lists all states that match the argument
"""

import MySQLdb
import sys


def safe_filter_states(username, password, dbname, state_name_searched):
    try:
        with MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password
            db=dbname
        ) as db:
            with db.cursor() as cursor:
                cursor.execute(
                        "SELECT * FROM states "
                        "WHERE BINARY name = %s "
                        "ORDER BY states.id ASC",
                        (state_name_searched,))
                for row in cursor.fetchall():
                    print(row)
    except MySQLdb.Error as e:
        print(f'Database error: {e}')


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
