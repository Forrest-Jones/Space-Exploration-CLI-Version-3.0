import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Planet
from helpers import get_planets_by_system, get_planets_by_distance, get_planet_by_name

engine = create_engine('sqlite:///space-exploration.db')
Session = sessionmaker(bind=engine)

@click.group()
def main():
    pass

# add this function
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

if __name__ == '__main__':
    main()

