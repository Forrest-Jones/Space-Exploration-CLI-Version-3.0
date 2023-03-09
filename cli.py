import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Planet
from helpers import get_planets_by_system, get_planets_by_distance, get_planet_by_name
from models import Planet, Astronomer


import os
import time
import pyfiglet

ROWS = 40    # Height of screen (lines)
COLS = 60    # Width of screen
HEIGHT = 10  # Height of ASCII rocket (lines)

ROCKET = """
      |
     / \\
    / _ \\
   |.o '.|
   |'._.'|
   |     |
   |     |
 ,'|  |  |`.
/  |  |  |  \\
|,-'--|--'-.|
"""

def initScreen():
    os.system(f"mode con cols={COLS} lines={ROWS}") # Set num cols and rows for window
    os.system("color 0a")   # Set color of window and text

def countDown():
    for count in range(10, 0, -1):
        os.system("clear")
        print(count)
        time.sleep(1)

def takeoff():
    for i in range(ROWS, HEIGHT, -1):
        os.system("clear")
        for j in range(i - HEIGHT, 0, -1):
            print()
        print(ROCKET)
        time.sleep(0.075)

    os.system("clear;printf '\033[3J'")
    ascii_text = pyfiglet.figlet_format("SPACE EXPLORATION CLI")
    for line in ascii_text.split("\n"):
        print(" " * ((COLS - len(line)) // 2) + line)
        time.sleep(1)

def main():
    initScreen()
    os.system("pause")
    os.system("clear")
    print("Prepare for takeoff...")
    time.sleep(2)
    countDown()
    os.system("clear")
    print("Liftoff!")
    time.sleep(2)
    takeoff()
    os.system("clear")
    print("We are now in orbit.")

if __name__ == "__main__":
    engine = create_engine('sqlite:///space-exploration.db')
    Session = sessionmaker(bind=engine)
    main()

@click.group()
def main():
    pass

@main.command()
@click.option('--name', prompt='Planet name', help='Name of the planet')
def find_planet(name):
    planet = get_planet_by_name(name)
    if planet:
        click.echo(f'{planet.name} ({planet.star_system}), {planet.distance} light years away')
    else:
        click.echo(f'{name} not found in the database')

@main.command()
@click.option('--name', prompt='Planet name', help='Name of the planet')
@click.option('--star-system', prompt='Star system', help='Name of the star system')
@click.option('--distance', prompt='Distance', help='Distance in light years', type=float)
def add_planet(name, star_system, distance):
    session = Session()
    planet = Planet(name=name, star_system=star_system, distance=distance)
    session.add(planet)
    session.commit()
    click.echo(f'{name} added to the database')

@main.command()
@click.option('--name', prompt='Planet name', help='Name of the planet')
def delete_planet(name):
    session = Session()
    planet = session.query(Planet).filter_by(name=name).first()
    if planet:
        session.delete(planet)
        session.commit()
        click.echo(f'{name} deleted from the database')
    else:
        click.echo(f'{name} not found in the database')

@main.command()
def list_planets():
    session = Session()
    planets = session.query(Planet).all()
    if planets:
        click.echo('List of planets:')
        for planet in planets:
            click.echo(f'- {planet.name} ({planet.star_system}), {planet.distance} light years away')
    else:
        click.echo('No planets found in the database')

@main.command()
@click.option('--system', help='Filter planets by star system')
@click.option('--distance', help='Filter planets by distance in light years', type=float)
def filter(system, distance):
    if system:
        planets = get_planets_by_system(system)
        click.echo(f'List of planets in the {system} system:')
        for planet in planets:
            click.echo(f'- {planet.name} ({planet.star_system}), {planet.distance} light years away')
    elif distance:
        planets = get_planets_by_distance(distance)
        click.echo(f'List of planets within {distance} light years:')
        for planet in planets:
            click.echo(f'- {planet.name} ({planet.star_system}), {planet.distance} light years away')
    else:
        click.echo('Please specify a filter')

@main.command()
@click.option('--name', prompt='Planet name', help='Name of the planet')
@click.option('--years', prompt='Years', help='Years of travel', type=int)
def time_dilation(name, years):
    planet = get_planet_by_name(name)
    if planet:
        time_passed = years * (1 - ((planet.distance ** 2) / (299792458 ** 2))) ** 0.5
        click.echo(f'Time passed on Earth: {time_passed} years')
    else:
        click.echo(f'{name} not found in the database')

@main.command()
def discoverers():
    session = Session()
    results = session.query(Astronomer, Planet).join(Planet, Astronomer.planet == Planet.name).all()
    session.close()

    click.echo('Astronomer\tPlanet')
    for row in results:
        click.echo(f'{row[0].name}\t\t{row[1].name} ({row[1].star_system})')

@main.command()
@click.option('--name', prompt='Planet name', help='Name of the planet')
@click.option('--speed', prompt='Spaceship speed (km/s)', help='Speed of the spaceship in km/s', type=float)
def travel_time(name, speed):
    planet = get_planet_by_name(name)
    if planet:
        distance = planet.distance * 9.4607e+12  # Convert light years to km
        time = distance / (speed * 1000)  # Convert km/s to km/h
        click.echo(f'Time to travel to {name} at {speed} km/s: {time} hours')
    else:
        click.echo(f'{name} not found in the database')

if __name__ == '__main__':
    main()
