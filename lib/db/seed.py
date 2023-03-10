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
        {'name': 'Robert T.A. Innes', 'planet': 'Proxima Centauri b', 'born': 1861},
        {'name': 'Michael Gillon', 'planet': 'TRAPPIST-1 e', 'born' : 1974},
        {'name': 'Kepler space telescope', 'planet': 'Kepler-442b', 'born': 2009},
        {'name': 'Nicola Astudillo-Defru', 'planet': 'LHS 1140b', 'born': 1985},
        {'name': 'Bonnard J. Teegarden', 'planet': 'Teegarden b', 'born': 1940},
        {'name': 'Xavier Bonfils', 'planet': 'Ross 128 b', 'born': 1978},
        {'name': 'Ansgar Reiners, Guillem Anglada-Escude', 'planet': 'Gliese 667 Cc', 'born': 1979},
        {'name': 'Kepler spacecraft', 'planet': 'K2-18 b', 'born': 2009},
        {'name': 'Duncan Wright', 'planet': 'Wolf 1061c', 'born': 1980},
        {'name': 'Emily Gilbert', 'planet': 'TOI 700d', 'born': 1993}        
    ]
    
    for astronomer in astronomers:
        astronomer_obj = Astronomer(name=astronomer['name'], planet=astronomer['planet'], born=astronomer['born'])
        session.add(astronomer_obj)

    session.commit()

    #time dilation works!

def insert_spaceships():
    spaceships = [
        {'name': 'Helios 2',                'planet': None,     'speed': 252792.536832,    'description': 'NASA Helios 2 space probe is the fastest man-made object ever. It set a record speed of 157078 mph during the mission. Helios 2 also has made a closer approach to the Sun than its predecessor. Helios 2 has looped around the Sun at a record distance of 0.29 AU from the surface. Helios 2 launched on January 15, 1976. It reached the orbit of Sun on 17th April 1976. The space probe sent back data about solar plasma, solar dust, cosmic rays and the electrical field to Earth until 23rd December 1979. Both Helios 1 and 2 space probes still remain in the orbit of the Sun.'},
        {'name': 'Helios 1',                'planet': None,     'speed': 228526.848,       'description': 'Helios 1 space probe was launched by NASA along with German space craft agency on 10th December 1974. The goal behind this mission was to study about solar processes. The NASA space probe managed to reach the Sun’s elliptical orbit. Helios 1 space probe has attained a speed of 142000 mph during the journey. This space probe orbit around the Sun at a distance of 1 AU(149597871 kilometers) from the surface. Helios 1 continued to send back data until 1982.'},
        {'name': 'Voyager 1',               'planet': None,     'speed': 62136.77184,      'description': 'Voyager I is the farthest traveled man-made the object to date. This space craft was launched back in 1977 with the mission of study about the outer solar system. On August 25, 2013, NASA Voyager 1 has successfully entered the interstellar space. During the mission, the Voyager 1 space craft attained a maximum speed of 38610 mph. It has also covered a record distance of 520 million kilometers every year. Voyager 1 space probe will continue the mission until 2025.'},
        {'name': 'New Horizons',            'planet': None,     'speed': 8536.669312,      'description': 'New Horizons is a space craft launched by NASA in 2006. The goal of this mission is to study about planet Pluto and its Moons. This probe has successfully flew 7800 miles above the Pluto on 14th July 2015. Thus, New Horizon has became the first space probe to explore the dwart planet Pluto. The space probe was launched on 19th January 2006. At that time, it has attained a record speed of 36373 mph, the highest launch speed than any other space craft. The mono propellants and gravitational assistants are main components that empowers the New Horizons space probe to attained such blazing launch speed.'},
        {'name': 'Stardust',                'planet': None,     'speed': 46439.230464,     'description': 'Stardust was a special space probe launched by NASA in 1999. The goal of this mission is to collect samples from comet wild 2 for laboratory analysis. This 300-kilogram, robotic probe attained a maximum speed of 28856 mph during that mission. That is, 6 times faster than the speed of bullet. Stardust has also successfully completed its primary mission in 2006. During the mission, stardust has traveled 2 billion miles to meet with the comet wild 2. The inbuilt rockets on the space craft powers it to make a swing in space to reach the comet.'},
        {'name': 'Apollo 10 Capsule',       'planet': None,     'speed': 39897.247104,     'description': 'Apollo 10 was a rehearsal mission by NASA before Lunar landing. During the return journey, on 26th May 1969 the Apollo 10 capsule acquired a blazing speed of 24791 mph. Guinness book of world records recognized Apollo 10 capsule as highest speed achieved by a manned vehicle. In fact, Apollo 10 module required such a blazing speed to reach Earth’s atmosphere from Lunar orbit. Apollo 10 also has completed the mission within 56.'},
        {'name': 'Discovery Space Shuttle', 'planet': None,     'speed': 28002.586,        'description': 'Space shuttle discovery held the record of a maximum number of successful missions than any other spacecraft in the history. The spacecraft has made 30 successful flights since 1984. It also held a record speed of 17400 miles per hour. That is, five times faster than the speed of a bullet. Sometimes spacecrafts have to travel faster than the normal speed of 17000 mph. Such conditions are depend on the orbit and altitude of spacecraft.'},
        {'name': 'Space Shuttle Columbia',  'planet': None,     'speed': 27358.848,        'description': 'Space shuttle Columbia was the first ever successful space shuttle in the history of space exploration. It has successfully completed 37 missions since 1981. During the missions, Space shuttle Columbia held a record speed of 17000 mph. The Space Shuttle Columbia outreached its normal speed when it crashed down on 1st February 2003. Normally, a space shuttle travels at a speed of 17000 mph to remain in the lower Earth orbit. At that speed, the crew of space shuttle can see Sunrise and Sunset a number of times within a single day.'},
        {'name': 'Nasa X43 - A',            'planet': None,     'speed': 11265.41,         'description': 'NASA X-43 A is an unmanned Hypersonic aircraft used to launch from a larger aircraft. In 2005, Guinness book of world records recognized NASA X-43 A as fastest aircraft ever made. It sets a top speed of 7000 miles per hour. That is about 8.4 times faster than the speed of sound. The NASA X-13 A uses a drop launch technology. At first, this hypersonic aircraft will bring to high altitude using larger aircraft and then dropped. With help of booster rocket, this aircraft would reach the target speed. At the final phase, after reaching the target speed NASA X-13 A balanced by its own engine.'},
        {'name': 'Rocket Sleds',            'planet': None,     'speed': 10385.1,          'description': 'Rocket sleds are actually testing platforms used to accelerate experimental objects. During tests, it create a record speed of 6453 mph. The rocket sleds use sliding pads instead of wheels to reach blazing speed. Rocket sleds are propelled using rockets. This external force makes an initial acceleration on experimental objects.The rocket sleds also have long straight track stretches over 10000 feet. The tank of rocket sleds also filled with lubricants like Helium gas so that the experimental object will reach to sufficient speed. Rocket sleds are commonly used to accelerate missiles, aircraft parts and emergency rescue sections of aircraft.'}
    ]

    for spaceship in spaceships:
        spaceship_obj = Spaceship(name=spaceship['name'], planet=spaceship['planet'], number=spaceship['number'], description=spaceship['description'])
        session.add(spaceship_obj)

    session.commit()