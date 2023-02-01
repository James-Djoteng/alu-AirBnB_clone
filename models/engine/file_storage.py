#!/usr/bin/python3
""" The file_storage module
"""
import json
from os import path
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """ A FileStorage class
    Attributes:
        __file_path: path to the file storage
        __objects: dictionary of class objects
    """
    __file_path = "file.json"
    __objects = {}

    existing_cls = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            "State": State
            }

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        keyy = obj.__class__.__name__ + "." + obj.id
        self.__objects[keyy] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_pddath)
        """
        newdict = {}
        for key in self.__objects:
            newdict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode='w') as f:
            json.dump(newdict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if path.isfile(self.__file_path):
            content = {}
            with open(self.__file_path, mode='r') as f:
                content = json.load(f)
                for k, v in content.items():
                    self.__objects[k] = self.existing_cls[(v['__class__'])](**v)

    def reset_obj(self):
        """Method that resets __objects attributes
        """
        self.__objects = {}
        