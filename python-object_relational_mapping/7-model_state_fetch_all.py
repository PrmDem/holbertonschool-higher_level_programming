#!/usr/bin/python3

"""fetches and prints all states
listed in the hbtn_0e_6_usa db.
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

    allStates = session.query(State).order_by(State.id).all()

    for item in allStates:
        print(f"{item.id}: {item.name}")
