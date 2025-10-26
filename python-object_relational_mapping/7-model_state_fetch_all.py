#!/usr/bin/python3
"""
Module 7 - All state model
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys

Base = declarative_base()

if __name__ == "__main__":
    # CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # create connection between sqlalchemy to mysql server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True)

    # bind engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all states sorted by id
    states = session.query(State).orderby(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

    # close session
    session.close()
