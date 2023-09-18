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


def validate_cls(args, cls, id=False):
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
    """ parse arg to it type """
    argv = re.sub("\"", "", arg)

    if is_int(argv):
        return int(argv)
    elif is_float(argv):
        return float(argv)
    else:
        return str(argv)


class_object = {
    "Amenity": Amenity,
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity,
    "BaseModel": BaseModel,
}


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    prompt = "(hbnb) "

    def default(self, arg):
        regex = re.search(r"\.", arg)

        console_arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        if regex:
            matchs = regex.span()
            args = [arg[:matchs[0]], arg[matchs[1]:]]
            regex = re.search(r"\((.*?)\)", args[1])
            if regex:
                console_command = [
                    args[1][:regex.span()[0]],
                    re.sub(",", "", re.sub("\"", "", regex.group()[1:-1]))
                    ]
                if console_command[0] in console_arg_dict.keys():
                    execute_args = "{} {}".format(args[0], console_command[1])
                    return console_arg_dict[console_command[0]](execute_args)

        return super().default(str(arg))

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
         Creates a new instance of BaseModelB%K,
         saves it (to the JSON file) and prints the id
        """
        args = arg.split()

        if not validate_cls(args, class_object):
            return

        models = class_object[args[0]]()
        storage.save()
        print(models.id)

    def do_show(self, arg):
        """
         Prints the string representation of an
         instance based on the class name and id
        """
        args = arg.split()

        if not validate_cls(args, class_object, True):
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

        if not validate_cls(args, class_object, True):
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
            if args[0] not in class_object:
                print("** class doesn't exist **")
                return
            print(["{}".format(str(values))
                  for values in obj_dict.values()
                   if type(values).__name__ == args[0]])

    def do_count(self, arg):
        args = arg.split()
        obj_dict = storage.all()
        count = 0

        for values in obj_dict.values():
            if args[0] == values.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
          Updates an instance based on the class name
          and id by adding or updating attribute
        """
        args = arg.split()

        if not validate_cls(args, class_object, True):
            return

        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        new_obj = obj_dict.get(key)

        if not new_obj:
            print("** no instance found **")
            return

        pattern = r'{(.*?)}'

        dict_like_string = ' '.join(args[2:])

        if re.search(pattern, dict_like_string):
            matches = re.findall(pattern, dict_like_string)

            split_arg = matches[0].split()
            dict_data = {}
            i = 0
            while (i < len(split_arg)):
                dict_data[re.sub("[:']", "", parse_type(
                    split_arg[i]))] = parse_type(split_arg[i+1])
                i += 2

            for keys, values in dict_data.items():
                print(keys, values)
                if keys in obj_dict[key].__class__.__dict__.keys():
                    val_type = type(obj_dict[key].__class__.__dict__[keys])
                    obj_dict[key].__dict__[keys] = val_type(values)
                else:
                    obj_dict[key].__dict__[keys] = values
            storage.save()
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        else:
            if args[2] in obj_dict[key].__class__.__dict__.keys():
                val_type = type(obj_dict[key].__class__.__dict__[args[2]])
                obj_dict[key].__dict__[args[2]] = parse_type(val_type(args[3]))
            else:
                obj_dict[key].__dict__[args[2]] = parse_type(args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
