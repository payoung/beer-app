from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy import Boolean, DateTime, Interval, Float
from sqlalchemy.orm import relationship, backref
from flask.ext.login import UserMixin
from database import Base


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

    beers = relationship('Beer', secondary='brewers')    


class Beer(Base):
    __tablename__ = 'beers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)

    brewers = relationship(User, secondary='brewers')
    recipes = relationship("Recipe", backref="beer")


class Brewer(Base):
    __tablename__ = 'brewers'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    beer_id = Column(Integer, ForeignKey('beers.id'), primary_key=True)
    user = relationship(User, backref=backref('users'))
    beer = relationship(Beer, backref=backref('beers'))

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    steep_time = Column(Integer)
    boil_time = Column(Integer)
    brew_date = Column(Date)
    secondary_date = Column(Date)
    bottle_date = Column(Date)

    beer_id = Column(Integer, ForeignKey('beers.id'))
    malts = relationship("Malt", backref="recipe")
    hops = relationship("Hop", backref="recipe")



class Malt(Base):
    __tablename__ = 'malts'

    id = Column(Integer, primary_key=True)
    variety = Column(String)
    weight = Column(Float)
    lbs_kg = Column(Boolean)
    milled = Column(Boolean)
    notes = Column(String)

    recipe_id = Column(Integer, ForeignKey("recipes.id"))


class Hop(Base):
    __tablename__ = 'hops'

    id = Column(Integer, primary_key=True)
    variety = Column(String)
    addition_time = Column(Integer)
    weight = Column(Float)
    oz_grams = Column(Boolean)
    fresh = Column(Boolean)
    notes = Column(String)    

    recipe_id = Column(Integer, ForeignKey("recipes.id"))
