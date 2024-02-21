#!/usr/bin/python3
"""
This script prints State objects
from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    create session and get first state
    from the db.
    """

    db_url = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(db_url)
    Session = sessionmaker(bind=db_url)
    session = Session()
    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print(first_state.id, first_state.name, sep=": ")
