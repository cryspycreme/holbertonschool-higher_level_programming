#!/usr/bin/python3
"""
Module 8 - First state model
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys


def get__first_state(username, password, dbname):
    """ Get first state"""
    # create connection between sqlalchemy to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # bind engine to the session class and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all states sorted by id
    try:
        state = session.query(State).order_by(State.id).first()
        if State is None:
            print("Nothing")
        else:
            print(f'{state.id}: {state.name}')
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    get_state(sys.argv[1], sys.argv[2], sys.argv[3])
