#!/usr/bin/python3
""" Define State """

from models.base_model import BaseModel


class State(BaseModel):
    """ Represent State """

    def __init__(self):
        super().__init__()
        self.name = ""
