#!usr/bin/python3

import datetime
import uuid
import models
import copy

class BaseModel:
    """
    Class BaseModel that defines all common atributes and methods
    """
    def __init__(self, *args, **kwargs):
        """
        Class generator
        args: non-keyworded argumaent
        lwargs: Keyworded argument list with keys and values
        """
        if args:
            self.id= str(uuid.uuid4())
            self.created_at= datetime.datetime.now()
            self.updated_at= datetime.datetime.now()
            models.storage.new(self)
        else:
            for (key, value) in kwargs:
                if key == "__class__":
                    continue
                
                elif key == "created_at" or key == "updated_at":
                    format="%Y%M%DT%H:%M:%S.%f"
                    value= datetime.datetime.strptime(value, format)
                    setattr(self, key, value)
    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()
    def to_dict(self):
        newDict= copy.deepcopy(self.__dict__)  
        newDict["__class__"]= self.__class__
        newDict["created_at"]= self.created_at.isoformat()
        newDict["updated_at"]= self.updated_at.isoformat()
        return (newDict)
