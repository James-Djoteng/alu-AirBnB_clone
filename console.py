#!/usr/bin/python3
"""
The console module
Command line entry point
"""
import cmd
import sys
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter
    """
    prompt = "(hbnb) "

    existing_cls = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            "State": State
            }

    def emptyline(self):
        """ emptyline overwrite
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        print()
        return True

    def do_create(self, args=None):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id"""
        newinstance = args.split()
        if not args or len(newinstance) == 0:
            print("** class name missing **")
        else:
            newinstance = self.existing_cls[newinstance[0]]()
            newinstance.save()
            print(newinstance.id)

    def do_show(self, args=None):
        """Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        line = args.split()
        if len(line) and line[0] not in self.existing_cls:
            print("** class doesn't exist **")
        elif len(line) == 0:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            instance = line[0] + "." + line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, args=None):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        line = args.split()
        if len(line) and line[0] not in self.existing_cls:
            print("** class doesn't exist **")
        elif len(line) == 0:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            instance = line[0] + "." + line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args=None):
        """Prints all string representation of all instances
        based or not on the class name"""
        line = args.split()
        temp = []
        if len(line) is not 0 and line[0] not in self.existing_cls:
            print("** class doesn't exist ** ")
            return
        if len(line) == 0:
            for key in models.storage.all():
                v = models.storage.all()[key]
                temp.append(str(v))
            if temp:
                print(temp)
        else:
            for key in models.storage.all():
                v = models.storage.all()[key]
                classname = key.split(".")
                if classname[0] == args:
                    temp.append(str(v))
            if temp:
                print(temp)

    def _int(self, stri):
        """
        Returns true if string can be casted to int
        """
        try:
            int(stri)
            return True
        except ValueError:
            return False

    def _float(self, stri):
        """
        Returns true if srting can be casted to float
        """
        try:
            float(stri)
            return True
        except ValueError:
            return False

    def do_update(self, args=None):
        """ Updates an instance based on the class na-
        me and id by adding or updating attribute
        (save the change into the JSON file)."""
        argz = args.split(" ", 3)
        if argz[0] and argz[0] not in self.existing_cls:
            print("** class doesn't exist **")
        elif not args:
            print("** class name missing **")
        elif len(argz) == 1:
            print("** instance id missing **")
        elif len(argz) == 2:
            print("** attribute name missing **")
        elif len(argz) == 3:
            print("** value missing **")
        else:
            objs = argz[0] + "." + argz[1]
            if objs in models.storage.all():
                """if self._int(argz[3]):
                argz[3] = int(argz[3])
                elif self._float(argz[3]):
                argz[3] = float(argz[3])
                if type(argz[3]) == str:"""
                setattr(models.storage.all()[objs], argz[2], argz[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """Overwrite of the system not recognizing arguments"""
        argz = line.split(".")
        showw = argz[1]
        show_w = showw[:4]
        splitting = showw.split("\"")
        counter = 0
        dest = argz[1][:7]
        if argz[1] == "all()":
            return self.do_all(argz[0])
        elif show_w == "show":
            param = argz[0] + " " + splitting[1]
            return self.do_show(param)
        elif dest == "destroy":
            param_d = argz[0] + " " + splitting[1]
            return self.do_destroy(param_d)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
