#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    # Close the session
    session.close()

