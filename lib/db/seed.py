from models import Planet
from models import Astronomer
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

def insert_astronomers():
    astronomers = [
        {'astronomer_name': 'Robert T.A. Innes', 'planet': 'Proxima Centauri b', 'born': 1861},
        {'astronomer_name': 'Michael Gillon', 'planet': 'TRAPPIST-1 e', 'born' : 1974},
        {'astronomer_name': 'Kepler space telescope', 'planet': 'Kepler-442b', 'born': 2009},
        {'astronomer_name': 'Nicola Astudillo-Defru', 'planet': 'LHS 1140b', 'born': 1985},
        {'astronomer_name': 'Bonnard J. Teegarden', 'planet': 'Teegarden b', 'born': 1940},
        {'astronomer_name': 'Xavier Bonfils', 'planet': 'Ross 128 b', 'born': 1978},
        {'astronomer_name': 'Ansgar Reiners, Guillem Anglada-Escude', 'planet': 'Gliese 667 Cc', 'born': 1979},
        {'astronomer_name': 'Kepler spacecraft', 'planet': 'K2-18 b', 'born': 2009},
        {'astronomer_name': 'Duncan Wright', 'planet': 'Wolf 1061c', 'born': 1980},
        {'astronomer_name': 'Emily Gilbert', 'planet': 'TOI 700d', 'born': 1993}        
    ]
    
    for astronomer in astronomers:
        astronomer_obj = Astronomer(name=astronomer['astronomer_name'], planet=astronomer['planet'], born=astronomer['born'])
        session.add(astronomer_obj)

    session.commit()

    #time dilation works!
