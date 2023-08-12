#!/usr/bin/python3
""" Define City """

from models.base_model import BaseModel


class City(BaseModel):
    """ Represent Define """

    def __init__(self):
        super().__init__()
        self.state_id = ""
        self.name = ""
