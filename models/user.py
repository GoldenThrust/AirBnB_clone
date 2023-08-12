#!/usr/bin/python3
""" Define User """

from models.base_model import BaseModel


class User(BaseModel):
    """ Represent User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
