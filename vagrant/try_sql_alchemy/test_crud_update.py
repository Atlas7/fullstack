from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Establish DB session
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# View prices for all veggieBurgers
veggieBurgers = session.query(MenuItem).filter_by(name="Veggie Burger")
print('\nView prices for all veggieBurgers\n')
for veggieBurger in veggieBurgers:
	print("MenuItem.id: ", veggieBurger.id)
	print("MenuItem.price: ", veggieBurger.price)
	print("MenuItem.restaurant.name: ", veggieBurger.restaurant.name)
	print("\n")

# At "Urban Burger", there are two veggieBurger items
# Our mission is the update the price of the first one (from $5.99 to $2.99)
# Note that the id number on your machine may be different to mine
# the ".one" at the end ensure SQL returns only one object, rather than a list.
print("\nChanging price for a veggieBurger at Urban Burger\n")
urbanVeggieBurger = session.query(MenuItem).filter_by(id=10).one()
print("urbanVeggieBurger.price (Before): ", urbanVeggieBurger.price)
urbanVeggieBurger.price = "$2.99"
session.add(urbanVeggieBurger)
session.commit()
print("urbanVeggieBurger.price (After): ", urbanVeggieBurger.price)

# View prices for all veggieBurgers again.
veggieBurgers = session.query(MenuItem).filter_by(name="Veggie Burger")
print('\nView prices for all veggieBurgers\n')
for veggieBurger in veggieBurgers:
	print("MenuItem.id: ", veggieBurger.id)
	print("MenuItem.price: ", veggieBurger.price)
	print("MenuItem.restaurant.name: ", veggieBurger.restaurant.name)
	print("\n")

# Change all veggieBurgers price to $2.99
print('\nChanging all veggieBurgers price to $2.99\n')
for veggieBurger in veggieBurgers:
	if veggieBurger.price != "$2.99":
		veggieBurger.price = "$2.99"
		session.add(veggieBurger)
		session.commit()

# View prices for all veggieBurgers again.
print('\nView prices for all veggieBurgers\n')
for veggieBurger in veggieBurgers:
	print("MenuItem.id: ", veggieBurger.id)
	print("MenuItem.price: ", veggieBurger.price)
	print("MenuItem.restaurant.name: ", veggieBurger.restaurant.name)
	print("\n")