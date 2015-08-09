from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Establish DB session
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete 'Spinach Ice Cream'
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
