from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.models import Base, User, Address

engine = create_engine("sqlite://", echo=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="spongebob squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="sandy squirrel",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="patrick star")

        session.add_all([spongebob, sandy, patrick])

        session.commit()
