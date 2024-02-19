#!/usr/bin/python3
"""
This script defines a State class model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State - class
    Attributes:
        __tablename__ (str): class table name
        id (int): The State id .
        name (str): The State name .
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
