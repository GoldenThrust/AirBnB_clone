#!/usr/bin/python3
""" BaseModel for airbnb """

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
        BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
            initial BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """
             updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
             returns a dictionary containing all keys/values of __dict__ of the instance
        """

        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__

        for keys, values in dict.items():
            if keys == "created_at" or keys == "updated_at":
                dict[keys] = values.isoformat()
            else:
                dict[keys] = values

        return dict

    def __str__(self):
        """
            print representation of basemodel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
