#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models

class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            city_list = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list