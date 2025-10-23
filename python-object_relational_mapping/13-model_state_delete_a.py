#!/usr/bin/python3

"""Deletes states from database
if their name contains the letter 'a'
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    removeStates = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in removeStates:
        session.delete(state)

    session.commit()
    session.close()
