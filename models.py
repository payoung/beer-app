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

    sensorunits = relationship('SensorUnit', backref='user')


class SensorUnit(Base):
    __tablename__ = 'sensorunits'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    sensors = relationship('Sensor', backref='sensorunit') 


class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dt_created = Column(DateTime)
    active = Column(Boolean)

    sensorunit_id = Column(Integer, ForeignKey('sensorunits.id'))
    profiles = relationship('Profile', secondary='sensortable')


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dt_created = Column(DateTime)
    num_sensors = Column(Integer)
    active = Column(Boolean)
    dt_stopped = Column(Integer)
    description = Column(String)

    sensors = relationship('Sensor', secondary='sensortable')
    notes = relationship('ProfileNote', backref='profile_note')


class SensorTable(Base):
    """ Association table between sensors and profiles"""
    __tablename__ = 'sensortable'

    sensor_id = Column(Integer, ForeignKey('sensors.id'), primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'), primary_key=True)
    sensor = relationship(Sensor, backref='sensor')
    profile = relationship(Profile, backref='profile')
    label = Column(String) # label for sensor, i.e. ambient vs fermentation


class ProfileNote(Base):
    __tablename__ = 'profile_notes'

    id = Column(Integer, primary_key=True)
    dt_created = Column(DateTime)
    dt_applied = Column(DateTime)
    note = Column(String)

    profile_id = Column(Integer, ForeignKey('profiles.id'))
