#!/usr/bin/python3

"""Defines State class which inherits from Base
and links to 'states' MySQL table
"""

if __name__ == "__main__":
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class State(Base):
        """Defines class State

        Args:
            id (int): unique identifier for a State instance
            name (str): name of the State instance
        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
