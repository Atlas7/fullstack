This is part of the Udacity - Full Stack Foundations exercise. On trying out SQLAlchemy.

# Database Setup

This section summarizes the general structure of `database_setup.py`.

```py
"""
General Structure:
=====================
database_setup.py
|- config begin
 |- class1
  |- table
  |- mapper
 |- class2
  |- table
  |- mapper
|- config end

################
## Config
################
Generally shouldn't change from project to project.

# config begin
- imports all modules needed
- creates instance of declarative base

# config end
- creates (or connects) the database and adds tables and columns.

################
## Class
################
- representation of table as a python class 
- extends the Base class
- nested inside will be table and mapper code

################
## Table
################
- representation of our table inside the database

syntax:
__tablename__ = "some_table"

################
## Mapper
################
- maps python objects to columns in our database

Example attributes:
- String(250)
- Integer
- relationship(Class)
- nullable = False
- primary_key = True
- ForeignKey("some_table.id")
"""
```
