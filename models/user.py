#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models import storage_type

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        # def __init__(self, *args, **kwargs):
        #     """ Initializes user """
        #     super().__init__(*args, **kwargs)
