#!/usr/bin/python3
"""
Script that lists all states that match the argument
"""
import MySQLdb
import sys


def state_name_matches_arg(username, password, dbname, state_name_searched):
    """
    Connect to MySQLdb and display all
    state names that input argument
    """
    try:
        with MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=dbname
                ) as db:
            with db.cursor() as cursor:
                query = (
                        "SELECT * FROM states"
                        "WHERE BINARY name = '{}' ORDER BY states.id ASC"
                        .format(state_name_searched))
                cursor.execute(query)
                for row in cursor.fetchall():
                    print(row)
    except MySQLdb.Error as e:
        print(f'Database errpr: {e}')


if __name__ == "__main__":
    state_name_matches_arg(sys.argv[1], sys.argv[2], sys.argv[3], sus.argv[4])
