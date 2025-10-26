#!/usr/bin/python3
"""
Module 13 - Delete states
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys


def delete_states_with_a(username, password, dbname):
    """ Get states that contain the letter a """
    # create connection between sqlalchemy to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # bind engine to the session class and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    try:
        # query the object to delete
        states = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .all()
                )
        if states is not None:
            # mark for deletion
            session.delete(states)
            # persist deletion
            session.commit()
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
