from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from flask.ext.login import UserMixin
from database import Base


brewers_table = Table('association', Base.metadata, 
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('beer_id', Integer, ForeignKey('beers.id'))
)


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

    brewers = relationship('Beer', secondary=brewers_table)    


class Beer(Base):
    __tablename__ = 'beers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)
