#!/usr/bin/python3
"""
BaseModel module have
class: BaseModel
def to_json(self)
"""
import uuid
import datetime
import models


class BaseModel:
    """ class BaseModel that defines all common
        attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ use *args, **kwargs arguments for the constructor
            of a BaseModel if kwargs is not empty each key
            of this dictionary is an attribute name
            (Note __class__ from kwargs is the only one that
            should not be added as an attribute.
            See the example output, below)
        """
        if kwargs != {} and kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = (datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"))
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>"""
        MyClass = self.__class__.__name__
        MyPrint = ("[{0}] ({1}) {2}".format(MyClass, self.id, self.__dict__))
        return (MyPrint)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        Dict = self.__dict__.copy()
        Dict['__class__'] = str(type(self).__name__)
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return (Dict)

    def delete(self):
        """Method to deletes an instance based on the class name"""
        models.storage.delete(self)
