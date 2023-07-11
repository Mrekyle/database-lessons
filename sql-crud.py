from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

"""
Building a brand new table in the database
"""

# Base table


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


"""
Populating the table with data
"""

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First programmer"
)

kyle_chart = Programmer(
    first_name="Kyle",
    last_name="Chart",
    gender="M",
    nationality="British",
    famous_for="Ninja"
)

jessica_leach = Programmer(
    first_name="Jessica",
    last_name="Leach",
    gender="F",
    nationality="British",
    famous_for="Girlfriend"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

# Adding each instance of data to the table session

# session.add(ada_lovelace)
# session.add(kyle_chart)
# session.add(jessica_leach)
# session.add(bill_gates)

# # Commiting to the session

session.commit()


# Updating a single record by searching for the specific data
# Then using '.' notation we update the object data

# programmer = session.query(Programmer).filter_by(id=4).first()
# programmer.famous_for = "Chocolate President"

# Commiting to the session. Each time a change or an update to the
# Database is needed/done

session.commit()

# Updating multiple entries at once. Like below we use a for loop to loop over
# the data and if they match the loop we tell it to do something. Like update
# the gender of the people in the database

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender Not Defined")

# session.commit()

# programmer = session.query(Programmer).filter_by(id=2).first()
# programmer.famous_for = "World President"

# programmer = session.query(Programmer).filter_by(id=3).first()
# programmer.famous_for = "Passenger Princess"

# session.commit()

"""
Deleting data from the database is diffucult to do from the front end 
where the user id or database id is not visable to the user to do so. 
So we can ask them to enter their information and by using that data
we can loop over the database to find the matching user and then delete
that users information.
"""

fname = input("Enter a first name: ")
lname = input("Enter a last name:")

# Searching the database for a matching pair of inputted data
programmer = session.query(Programmer).filter_by(
    first_name=fname, last_name=lname).first()
if programmer is not None:
    # If the data is found, then it will print out the corisponding data
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete your profile? (y/n)")
    if confirmation.lower() == "y":  # if the user enters Y or y the data will be deleted
        session.delete(programmer)
        session.commit()
        print("Programmers information has been deleted")
    else:
        print("Programmer has not been deleted")
else:
    # If nothing is found it will print out
    print("No Records Found")


# Query the database to find all programmers in the database

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
