from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Planet

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
