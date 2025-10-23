#!/usr/bin/python3

"""fetches and prints either the first state
listed in the hbtn_0e_6_usa db; or 'Nothing'.
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

    firstState = session.query(State).first()

    if firstState:
        print(f"{firstState.id}: {firstState.name}")
    else:
        print("Nothing")
