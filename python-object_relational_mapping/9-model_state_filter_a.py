#!/usr/bin/python3

"""fetches from 'hbtn_0e_6_usa'
states with the letter 'a' in their name.
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

    aStates = (session.query(State)
               .filter(State.name.like('%a%'))
               .order_by(State.id).all())

    for state in aStates:
        print(f"{state.id}: {state.name}")

    session.close()
