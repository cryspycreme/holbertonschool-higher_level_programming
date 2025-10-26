#!/usr/bin/python3
"""
Module 10 - Get a state
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys


def get_matched_state_id(username, password, dbname, state_name):
    """ Get state ID that match name """
    # create connection between sqlalchemy to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # bind engine to the session class and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    try:
        states = (
                session.query(State)
                .filter(State.name == state_name)
                .first()
                )
        if states is None:
            print("Not found")
        else:
            print(states.id)
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    get_matched_state_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
