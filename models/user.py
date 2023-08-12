#!/usr/bin/python3
""" Define User """

from models.base_model import BaseModel


class User(BaseModel):
    """ Represent User """

    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
