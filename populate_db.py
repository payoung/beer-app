""" Add some test data to database """

from database import db_session
from models import User, SensorUnit, Sensor, Profile, SensorTable, ProfileNote
from datetime import datetime


def add_data():
    
    # Add User:

    user1 = User(name="superuser", email="fake@email.com", password="password",
                 phone="+16509119111")

    # Add the Sensor Units:

    unit1 = SensorUnit(name="katies-kitchen", user=user1)
    unit2 = SensorUnit(name="pauls-house", user=user1)

    # Add the Sensors:

    sensor1 = Sensor(name="2882E92D6008F", 
                     dt_created=datetime(2014, 12, 27, 0, 0, 0, 0),
                     active=1, sensorunit=unit1)
    sensor2 = Sensor(name="28FFEB6760144E7",
                     dt_created=datetime(2015, 1, 25, 0, 0, 0, 0),
                     active=1, sensorunit=unit1)
    sensor3 = Sensor(name="28FF1F51601441F",
                     dt_created=datetime(2015, 1, 18, 0, 0, 0, 0),
                     active=1, sensorunit=unit2)
    sensor4 = Sensor(name="28FFC81D60144E2",
                     dt_created=datetime(2015, 1, 18, 0, 0, 0, 0),
                     active=1, sensorunit=unit2)

    # Add Fermentation Temperature Profiles:

    profile1 = Profile(name="Test Profile", 
                       dt_created=datetime(2014, 12, 27, 14, 0, 0, 0),
                       num_sensors=1, active=0,
                       dt_stopped=datetime(2015, 1, 12, 1, 50, 0, 0), 
                       description="""This profile is a test run of the sensor and was montiroing 
                                    the ambient temperature in the room, not an active 
                                    fermentation. This gives a good baseline for what the ambient 
                                    temperature will look like, so I can compare the fluctuations 
                                    in ambient due to space conditioning, with the fluctuations 
                                    when it is hooked up to an actual fermentation.""")
    st1 = SensorTable(sensor=sensor1, profile=profile1, label="Ambient")
    profile2 = Profile(name="Single Hop Cascade",
                       dt_created=datetime(2015, 1, 12, 1, 52, 0, 0),
                       num_sensors=1, active=0,
                       dt_stopped=datetime(2015, 1, 24, 19, 30, 0, 0),
                       description="""Currently the temperature sensor is hooked up to a one 
                                    gallon batch of a single hop pale ale. The sensor was attached 
                                    to the outside of the fermentation carboy, and I used a piece 
                                    of packing foam to insulate the sensor from the ambient 
                                    conditions. Based on the fluctuations observed during the test 
                                    run, it appears that the insulation is working as intended.""")
    st2 = SensorTable(sensor=sensor1, profile=profile2, label="Fermentation")
    profile3 = Profile(name="Single Hop Sorachi",
                       dt_created=datetime(2015, 1, 25, 1, 30, 0, 0),
                       num_sensors=2, active=1,
                       dt_stopped=datetime.now(),
                       description="""Currently the temperature sensors are hooked up to a one 
                                    gallon batch of Single Hop (Sorachi Ace) Pale Ale. I brewed two 
                                    single hop batches in the same session (the other with 
                                    Amarillo), and hooked up the fementation sensor to the Sorachi 
                                    carboy. The other sensor is monitoring ambient temperature.""")
    st3 = SensorTable(sensor=sensor1, profile=profile3, label="Ambient")
    st4 = SensorTable(sensor=sensor2, profile=profile3, label="Fermentation")
    profile4 = Profile(name="Imperial Stout",
                       dt_created=datetime(2015, 1, 18, 13, 0, 0, 0),
                       num_sensors=2, active=0,
                       dt_stopped=datetime(2015, 2, 1, 2, 34, 0, 0),
                       description="""Currently the temperature sensors are hooked up to a five 
                                    gallon batch of an Imperial Stout. One sensor is attached to 
                                    the fermentation bucket, with some foam insulation on the back, 
                                    and the other temperature sensor is recording the ambient 
                                    conditions.""")
    st5 = SensorTable(sensor=sensor3, profile=profile4, label="Ambient")  # need to check this
    st6 = SensorTable(sensor=sensor4, profile=profile4, label="Fermentation") # need to check this
    profile5 = Profile(name="Honey Ale",
                       dt_created=datetime(2015, 2, 1, 2, 35, 0, 0),
                       num_sensors=2, active=0,
                       dt_stopped=datetime.now(),
                       description="""Currently the temperature sensors are hooked up to a five 
                                    gallon batch of an honey ale. One sensor is attached to the 
                                    fermentation bucket, with some foam insulation on the back, and 
                                    the other temperature sensor is recording the ambient 
                                    conditions.""")
    st7 = SensorTable(sensor=sensor3, profile=profile5, label="Ambient") # need to check this
    st8 = SensorTable(sensor=sensor4, profile=profile5, label="Fermentation") # need to check this

    # Add some Notes for the Profiles:

    note1 = ProfileNote(dt_created=datetime(2015, 1, 12, 2, 30, 0, 0),
                        dt_applied=datetime(2015, 1, 12, 2, 30, 0, 0),
                        note="""Pitched the Yeast way too hot, probably should have cooled the wort 
                             a few more degrees.""",
                        profile_note=profile2)
    note2 = ProfileNote(dt_created=datetime(2015, 1, 18, 2, 0, 0, 0),
                        dt_applied=datetime(2015, 1, 18, 2, 0, 0, 0),
                        note="""Updated the Arduino/Python code, but wasn't able to update this 
                              sensor unit remotely, so the unit went offline for a bit.""",
                        profile_note=profile2)

    db_session.add_all([unit1, unit2, sensor1, sensor2, sensor3, sensor4, 
                        profile1, profile2, profile3, profile4, st1, st2, st3,
                        st4, st5, st6, st7, st8, note1, note2])
    db_session.commit()


if __name__ == "__main__":
    add_data()
