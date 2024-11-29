#!/usr/bin/python3
"""
Writes out the State object with the name passed as argument from the db
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine  #This ensure that the create engine is imported.
from sqlalchemy.orm import sessionmaker # The session maker is being imported.


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'. # Directs the creation of engine creation.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not state else state.id)
