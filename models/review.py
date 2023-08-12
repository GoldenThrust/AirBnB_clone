#!/usr/bin/python3
""" Define Review """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Represent Review """

    place_id = ""
    user_id = ""
    text = ""
