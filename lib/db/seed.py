from models import Planet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///space-exploration.db')
Session = sessionmaker(bind=engine)
session = Session()

def insert_planets():
    planets = [
        {'name': 'Proxima Centauri b', 'star_system': 'Alpha Centauri', 'distance': 4.24},
        {'name': 'TRAPPIST-1 e', 'star_system': 'TRAPPIST-1', 'distance': 39.6},
        {'name': 'Kepler-442b', 'star_system': 'Kepler-442', 'distance': 1200},
        {'name': 'LHS 1140b', 'star_system': 'LHS 1140', 'distance': 40},
        {'name': 'Teegarden b', 'star_system': 'Teegarden', 'distance': 12.5},
        {'name': 'Ross 128 b', 'star_system': 'Ross 128', 'distance': 11},
        {'name': 'Gliese 667 Cc', 'star_system': 'Gliese 667 C', 'distance': 23.6},
        {'name': 'K2-18 b', 'star_system': 'K2-18', 'distance': 124},
        {'name': 'Wolf 1061c', 'star_system': 'Wolf 1061', 'distance': 14.1},
        {'name': 'TOI 700 d', 'star_system': 'TOI 700', 'distance': 101},
    ]

    for planet in planets:
        planet_obj = Planet(name=planet['name'], star_system=planet['star_system'], distance=planet['distance'])
        session.add(planet_obj)

    session.commit()
