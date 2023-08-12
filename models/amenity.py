#!/usr/bin/python3
""" Define Amenities """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represent Amenity """

    def __init__(self):
        super().__init__()
        self.name = ""
