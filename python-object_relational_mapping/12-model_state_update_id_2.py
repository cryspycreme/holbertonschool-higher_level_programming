#!/usr/bin/python3
"""
Module 11 - Add a new state
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys


def add_state(username, password, dbname):
    """ Adds a state to the database """
    # create connection between sqlalchemy to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # bind engine to the session class and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    try:
        state = session.query(State).filter(State.id == 2).first
        if state is not None:
            state.name = 'New Mexico'
            session.commit()
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    add_state(sys.argv[1], sys.argv[2], sys.argv[3])
