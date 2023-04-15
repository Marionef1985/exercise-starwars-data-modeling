import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    fisrt_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    id_favorites_planets = Column(Integer, ForeignKey('favorites_planets.planet_id'))
    id_favorite_character = Column(Integer, ForeignKey('favorite_characters.character_id'))

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    name = Column(String(20), ForeignKey('planets.name'))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    name = Column(String(20), ForeignKey('characters.name'))
    


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name = Column(String(250))
    population  = Column(String(250))
    terrain = Column(String(250))
    description = Column(String(500))
    climate = Column(String(250))
    oribit_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name = Column(String(20))
    gender = Column(String(10))
    eye_color = Column(String(10))
    hair_color   = Column(String(10))
    description = Column(String(500))
    birthday = Column(String(10))
    height = Column(Integer)
    skin_color = Column(String)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
