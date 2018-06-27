# Catalog App

The catalog app creates an empty sports equipment database.  Users can login in with their google plus account, which will give them the ability to create, update, and delete items from the database.  Non-users can view the database.  The preset categories
are: Soccer, Baseball, Football, Snowboarding, Hockey, and Weight Training.


## Prerequisites
Python 2.7 or above


### Getting Started
There are two ways to get started: start with categories only or start with a populated database with items for demo purposes.  

#### Demo Instructions (prefilled items)
1. Run database_setup.py to set up the database.
2. Run lotsofitems.py to populate database with categories and items.
3. Run catalog.py and go to localhost:5000.

WARNING: YOU WILL ONLY BE ABLE TO EDIT OR DELETE NEW ITEMS YOU CREATE NOT THE EXISTING ONES FROM lotsofitems.py.

#### Demo Instructions (categories only)
1. Run database_setup.py to set up the database.
2. Run categories_only.py to populate database with categories only.
3. Run catalog.py and go to localhost:5000.
4. Login in with google plus and begin by adding items.


#### Acknowledgements
 * code for google plus login was taken from Udacity's course-The Backend: Databases and Applications: Creating Google Sign in.
