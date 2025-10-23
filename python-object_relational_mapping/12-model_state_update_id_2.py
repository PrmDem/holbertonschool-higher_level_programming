#!/usr/bin/python3

"""Changes name of state with id '2'
to 'New Mexico'.
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

    updatedState = session.query(State).filter_by(id=2).first()
    updatedState.name = 'New Mexico'

    session.commit()
    session.close()
