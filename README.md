# Space Exploration CLI

#Space Exploration CLI

#Introduction

#This is a CLI app that allows users to explore information about planets in a database. The app can perform the following actions:

    find_planet: Find a planet by its name and display its star system and distance in light years.

    add_planet: Add a new planet to the database with its name, star system, and distance in light years.

    delete_planet: Delete a planet from the database by its name.

    list_planets: List all the planets present in the database along with their star system and distance in light years.

    filter: Filter the planets in the database by either star system or distance.

    time_dilation: Calculate the time passed on Earth for a given number of years passed on a planet, taking into account time dilation due to the planet's distance from Earth.


#Directory Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── cli.py
├── db
│ ├── alembic.ini
│ ├── models.py
│ └── seed.py
├── debug.py
└── helpers.py

#Getting Started

#Fork and clone this repository.

#Set up a virtual environment with pipenv.

#Install dependencies with pipenv install (**See below for copy paster pip install**).

#Create the database with alembic upgrade head.

#Seed the database with python lib/db/seed.py.

#Run the CLI with python lib/cli.py.

#ALL DEPENDENCIES CAN BE INSTALLED WITH ONE COMMAND(copy and paste the following in its entirety to your terminal):

**"pip install aesara-theano-fallback==0.1.0 alembic==1.10.1 appnope==0.1.3 arviz==0.12.1 astropy==5.2.1 asttokens==2.2.1 backcall==0.2.0 cachetools==5.3.0 cftime==1.6.2 click==8.1.3 contourpy==1.0.7 cycler==0.11.0 decorator==5.1.1 deprecat==2.1.1 dill==0.3.6 executing==1.2.0 exoplanet==0.5.3 exoplanet-core==0.1.2 Faker==17.6.0 fastprogress==1.0.3 filelock==3.9.0 fonttools==4.39.0 importlib-metadata==6.0.0 importlib-resources==5.12.0 ipdb==0.13.11 ipython==8.11.0 jedi==0.18.2 kiwisolver==1.4.4 Mako==1.2.4 MarkupSafe==2.1.2 matplotlib==3.7.1 matplotlib-inline==0.1.6 netCDF4==1.6.3 numpy==1.21.6 packaging==23.0 pandas==1.5.3 parso==0.8.3 patsy==0.5.3 pexpect==4.8.0 pickleshare==0.7.5 Pillow==9.4.0 prompt-toolkit==3.0.38 ptyprocess==0.7.0 pure-eval==0.2.2 pyerfa==2.0.0.1 pyfiglet==0.8.post1 Pygments==2.14.0 pymc3==3.11.5 pyparsing==3.0.9 python-dateutil==2.8.2 pytz==2022.7.1 PyYAML==6.0 scipy==1.7.3 semver==2.13.0 six==1.16.0 SQLAlchemy==2.0.5.post1 stack-data==0.6.2 Theano-PyMC==1.1.2 tomli==2.0.1 traitlets==5.9.0 typing_extensions==4.5.0 wcwidth==0.2.6 wrapt==1.15.0 xarray==2023.1.0 xarray-einstats==0.5.1 zipp==3.15.0"**

#Usage

To use the app, the user needs to run the Python script followed by the command and any required options and arguments. For example, to add a new planet to the database, the user can type:

    "python cli.py add-planet"

#find_planet: Find a planet by its name and display its star system and distance in light years.

#add_planet: Add a new planet to the database with its name, star system, and distance in light years.

#delete_planet: Delete a planet from the database by its name.

#list_planets: List all the planets present in the database along with their star system and distance in light years.

#filter: Filter the planets in the database by either star system or distance.

#time_dilation: Calculate the time passed on Earth for a given number of years passed on a planet, taking into account time dilation due to the planet's distance from Earth.

#The available commands are:

    find_planet: Find a planet by its name and display its star system and distance in light years. The user can invoke this command by typing: python lib/cli.py find_planet --name <planet_name>

    add_planet: Add a new planet to the database with its name, star system, and distance in light years. The user can invoke this command by typing: python lib/cli.py add_planet --name <planet_name> --star-system <star_system_name> --distance <distance>

    delete_planet: Delete a planet from the database by its name. The user can invoke this command by typing: python lib/cli.py delete_planet --name <planet_name>

    list_planets: List all the planets present in the database along with their star system and distance in light years. The user can invoke this command by typing: python lib/cli.py list_planets

    filter: Filter the planets in the database by either star system or distance. The user can invoke this command by typing: python lib/cli.py filter --system <star_system_name> to filter  by star system, or `python lib/cli.py filter --distance




###Here is an exhaustive list of command functionality:

find_planet: Find a planet by its name and display its star system and distance in light years. The user can invoke this command by typing: python lib/cli.py find_planet --name <planet_name>

add_planet: Add a new planet to the database with its name, star system, and distance in light years. The user can invoke this command by typing: python lib/cli.py add_planet --name <planet_name> --star-system <star_system_name> --distance <distance>

delete_planet: Delete a planet from the database by its name. The user can invoke this command by typing: python lib/cli.py delete_planet --name <planet_name>

list_planets: List all the planets present in the database along with their star system and distance in light years. The user can invoke this command by typing: python lib/cli.py list_planets

filter: Filter the planets in the database by either star system or distance. The user can invoke this command by typing: python lib/cli.py filter --system <star_system_name> to filter by star system, or python lib/cli.py filter --distance <distance> to filter by distance.

time_dilation: Calculate the time passed on Earth for a given number of years passed on a planet, taking into account time dilation due to the planet's distance from Earth. The user can invoke this command by typing: python lib/cli.py time_dilation --name <planet_name> --years <years>

discoverers: List all astronomers and the planets they discovered. The user can invoke this command by typing: python lib/cli.py discoverers

travel_time: Calculate the time required to travel to a planet at a given spaceship speed. The user can invoke this command by typing: python lib/cli.py travel_time --name <planet_name> --speed <spaceship_speed>

#Eleanor and Tyler:  "Thank you for shopping with us. Wasn't it out of this world?" 