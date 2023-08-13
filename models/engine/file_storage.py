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

class_object = {
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity,
    "BaseModel": BaseModel
}


class FileStorage:
    """
        Serislizes instances to a JSON file and
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        airbnb_objdict = {
            keys:
            values.to_dict() for keys, values in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(airbnb_objdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:
                airbnb_dict = json.load(f)
                for values in airbnb_dict.values():
                    cls_name = values["__class__"]
                    if cls_name in class_object:
                        cls = class_object[cls_name]
                        del values["__class__"]
                        new_obj = cls(**values)
                        self.new(new_obj)
        except FileNotFoundError:
            pass
