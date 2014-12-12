from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy import Boolean, DateTime
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


class Brewer(Base):
    __tablename__ = 'brewers'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    beer_id = Column(Integer, ForeignKey('beers.id'), primary_key=True)
    user = relationship(User, backref=backref('users'))
    beer = relationship(Beer, backref=backref('beers'))
