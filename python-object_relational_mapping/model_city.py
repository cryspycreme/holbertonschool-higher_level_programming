#!/usr/bin/python3
"""
Module 14 - Cities in State
"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State


class City(Base):
    """ City class linked to 'cities' table in MySQL"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", backref="cities")
