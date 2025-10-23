#!/usr/bin/python3

"""prints all cities from hbtn_0e_14_usa
following the format <state name>: (<city id>) <city name>
ordered by ascending city id
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for City, State in (session.query(City, State)
                        .join(State, City.state_id == State.id)
                        .order_by(City.id).all()):
        print(f"{State.name}: ({City.id}) {City.name}")
