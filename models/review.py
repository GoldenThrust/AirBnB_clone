#!/usr/bin/python3
""" Define Review """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Represent Review """

    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
