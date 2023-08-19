#!/usr/bin/python3
"""Below is the amenity class with imported modules"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """The class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # place_amenities = relationship('Place', secondary='place_amenity')
