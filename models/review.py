#!/usr/bin/python3
""" Reviews the module for the AirBnB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Reviews the class to store the review information """
    place_id = ""
    user_id = ""
    text = ""
