#!/usr/bin/python3
"""
Module 14 - Cities in state
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
from model_city import City
import sys


def fetch_city_by_state(username, password, dbname):
    """ Get states that contain the letter a """
    # create connection between sqlalchemy to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # bind engine to the session class and create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    try:
        # query the object and return results in tuples
        results = (
                session.query(State, City)
                .join(City, City.state_id == State.id)
                .order_by(City.id)
                .all()
                )
        for city, state in results:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        # close session
        session.close()


if __name__ == "__main__":
    fetch_city_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
