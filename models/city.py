#!/usr/bin/python3
""" The City Module for AirBnB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
