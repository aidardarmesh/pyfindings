from sqlalchemy import select
from sqlalchemy.orm import Session

from database.engine import engine
from database.models import User

session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

