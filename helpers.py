from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Planet
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('sqlite:///space-exploration.db')
Session = sessionmaker(bind=engine)

def get_planets_by_system(system):
    session = Session()
    planets = session.query(Planet).filter_by(star_system=system).all()
    session.close()
    return planets

def get_planets_by_distance(distance):
    session = Session()
    planets = session.query(Planet).filter(Planet.distance <= distance).all()
    session.close()
    return planets

def get_planet_by_name(name):
    session = Session()
    planet = session.query(Planet).filter_by(name=name).first()
    session.close()
    return planet

def time_to_planets(spacecraft_name, speed_mph):
    time_to_planet = {}
    planets = session.query(Planet).all()
    for planet in planets:
        distance_miles = planet.distance * 5.87849981e+12 # convert light years to miles
        time_hours = distance_miles / speed_mph
        time_to_planet[planet.name] = time_hours
    return time_to_planet