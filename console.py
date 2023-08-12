#!/usr/bin/python3
"""  entry point of the command interprete """

import re
import cmd
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


def validate_cls(args, cls, id=False) -> bool:
    """ validate HBNBCommand method argument """
    if not args:
        print("** class name missing **")
        return False
    if args[0] not in cls:
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and id:
        print("** instance id missing **")
        return False
    return True


def is_float(typ):
    """ checks if typ is float """
    try:
        tmp = float(typ)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(typ):
    """ checks if typ is int """
    try:
        tmp = int(typ)
    except (TypeError, ValueError):
        return False
    else:
        return True


def parse_type(arg):
    """ parse arg to an to basic type """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return parsed


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "
        self.__class_object = {
            "User": User,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
            "BaseModel": BaseModel,
        }

    def emptyline(self):
        """ Do nothing """
        pass

    def do_quit(self, arg):
        """ exit the program """
        return True

    def do_EOF(self, arg):
        """ exit the program """
        return True

    def do_create(self, arg):
        """
         Creates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id
        """
        args = arg.split()

        if not validate_cls(args, self.__class_object):
            return

        models = self.__class_object[args[0]]()
        storage.save()
        print(models.id)

    def do_show(self, arg):
        """
         Prints the string representation of an
         instance based on the class name and id
        """
        args = arg.split()

        if not validate_cls(args, self.__class_object, True):
            return

        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        new_obj = obj_dict.get(key)

        if not new_obj:
            print("** no instance found **")
            return

        print(new_obj)

    def do_destroy(self, arg):
        """
          Deletes an instance based on the class
          name and id (save the change into the JSON file)
        """
        args = arg.split()

        if not validate_cls(args, self.__class_object, True):
            return

        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        new_obj = obj_dict.get(key)

        if not new_obj:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """
          Prints all string representation of all instances
          based or not on the class name
        """
        args = arg.split()
        obj_dict = storage.all()

        if not arg:
            print(["{}".format(str(values)) for values in obj_dict.values()])
        else:
            if args[0] not in self.__class_object:
                print("** class doesn't exist **")
                return
            print(["{}".format(str(values))
                  for values in obj_dict.values()
                   if type(values).__name__ == args[0]])

    def do_update(self, arg):
        """
          Updates an instance based on the class name
          and id by adding or updating attribute
        """
        args = arg.split()

        if not validate_cls(args, self.__class_object, True):
            return

        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        new_obj = obj_dict.get(key)

        if not new_obj:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        if args[2] in obj_dict[key].__class__.__dict__.keys():
            val_type = type(obj_dict[key].__class__.__dict__[args[2]])
            obj_dict[key].__dict__[args[2]] = val_type
        else:
            obj_dict[key].__dict__[args[2]] = parse_type(args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
