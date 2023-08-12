#!/usr/bin/python3
"""
    File Storage class for the airbnb
"""
import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
        Serislizes instances to a JSON file and
        deserializes JSON file to instances
    """

    def __init__(self):
        """ initialize new instance of filestorage """
        self.__file_path = "airbnb.json"
        self.__objects = {}
        self.__class_object = {
            "User": User,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
            "BaseModel": BaseModel
        }

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        airbnb_objdict = {
            keys:
            self.__objects[keys].to_dict() for keys in self.__objects.keys()
        }
        with open(self.__file_path, "w") as f:
            json.dump(airbnb_objdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                airbnb_dict = json.load(f)
                for values in airbnb_dict.values():
                    cls_name = values["__class__"]
                    if cls_name in self.__class_object:
                        cls = self.__class_object[cls_name]
                        del values["__class__"]
                        new_obj = cls(**values)
                        self.new(new_obj)
        except FileNotFoundError:
            pass
