from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Establish DB session
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add a new Restaurant object (row)
myFirstRestaurant = Restaurant(name = "Pizza Palare")
session.add(myFirstRestaurant)
session.commit()
print session.query(Restaurant).all()

# Add a new MenuItem object (row)
cheesepizza = MenuItem(
	name="Cheese Pizza",
	description="Made with all natural ingredients and fresh mozzarella",
	course="Entree",
	price="$8.99",
	restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
print session.query(MenuItem).all()