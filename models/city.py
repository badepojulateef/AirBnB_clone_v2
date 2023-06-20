#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
<<<<<<< HEAD
from sqlalchemy.orm import relationship
from sqlalchemy import storage_type
=======
>>>>>>> parent of be54c57... added task 8


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    if storage_type == 'db':

        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        places = relationship(
            "Place", backref="cities", cascade="all, delete-orphan"
        )
    else:
        name = ""
        state_id = ""
        
        def __init__(self, *args, **kwargs):
            """ Initializes city """
            super().__init__(*args, **kwargs)
=======
    __tablename__= 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
>>>>>>> parent of be54c57... added task 8
