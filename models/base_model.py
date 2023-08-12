#!/usr/bin/python3
""" BaseModel for airbnb """

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ initial new instance of BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for keys, values in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    self.__dict__[keys] = datetime.strptime(values, format)
                else:
                    self.__dict__[keys] = values
        else:
            models.storage.new(self)

    def save(self):
        """
             updates the public instance attribute
             updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
             returns a dictionary containing all
             keys/values of __dict__ of the instance
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
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
