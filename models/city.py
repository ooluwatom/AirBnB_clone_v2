#!/usr/bin/python3
"""The city class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    # Initialize class for file/db storage type
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete', backref='cities')
