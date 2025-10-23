#!/usr/bin/python3

"""prints id of the state passed as argument
or 'Not found' if not in the database.
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

    thatState = session.query(State).filter(State.name == sys.argv[4]).first()

    if thatState:
        print(f"{thatState.id}")
    else:
        print("Not found")

    session.close()
