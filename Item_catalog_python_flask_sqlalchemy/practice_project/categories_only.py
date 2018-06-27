from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import SportCategory, Base, SportItem
engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add Soccer Category
category1 = SportCategory(name="Soccer")
session.add(category1)
session.commit()

# Add Baseball Category
category1 = SportCategory(name="Baseball")
session.add(category1)
session.commit()

# Add Football Category
category1 = SportCategory(name="Football")
session.add(category1)
session.commit()

# Add Snowboarding Category
category1 = SportCategory(name="Snowboarding")
session.add(category1)
session.commit()

# Add Hockey Category
category1 = SportCategory(name="Hockey")
session.add(category1)
session.commit()

# Add Weight Training Category
category1 = SportCategory(name="Weight Training")
session.add(category1)
session.commit()

print "Categories added successfully"
