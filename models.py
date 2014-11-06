from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, Boolean, DateTime
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

    brewers = relationship('Brewer', backref='user', lazy='dynamic')    


class Beer(Base):
    __tablename__ = 'beers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)

    user_id = Column(Integer, ForeignKey('users.id')

"""

class Brewer(Base):
    __tablename__ = 'brewers'

    id = Column(Integer, primary_key=True)

"""


    
    
    


