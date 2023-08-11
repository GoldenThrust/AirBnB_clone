#!/usr/bin/python3
"""  entry point of the command interprete """
import cmd
from models import storage
from models.base_model import BaseModel
def validate_cls(args, cls, id=False) -> bool:
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

class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "
        self.__class_object = {
            "BaseModel": BaseModel
        }

    def emptyline(self):
        """ Do nothing """
        pass

    def do_quit(self, arg) :
        """ exit the program """
        return True
    
    def do_EOF(self, arg):
        """ exit the program """
        return True
    
    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = arg.split()

        if not validate_cls(args, self.__class_object):
            return

        models = self.__class_object[args[0]]()
        storage.save()
        print(models.id)
    
    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id """
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
        """ Deletes an instance based on the class name and id (save the change into the JSON file) """
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
        """  Prints all string representation of all instances based or not on the class name """
        args = arg.split()
        obj_dict = storage.all()
    
        if not arg:
            print(["{}".format(str(values)) for values in obj_dict.values()])
        else:
            if args[0] not in self.__class_object:
                print("** class doesn't exist **")
                return
            print(["{}".format(str(values)) for values in obj_dict.values() if type(values).__name__ == args[0]])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
