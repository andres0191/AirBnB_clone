#!/usr/bin/python3
"""Base Class for all Models
"""
import uuid
from datetime import datetime
import models
Time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
        """Base Model for other Classes
        """
        def __init__(self, *args, **kwargs):
                """Id assigned when an instance is created
                """
                if kwargs != {} and kwargs is not None:
                        for key, value in kwargs.items():
                                if key == "created_at" or key == "updated_at":
                                        value = datetime.strptime(value, Time)
                                        if key != "__class__":
                                                setattr(self, key, value)
                else:
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime.today()
                        self.updated_at = datetime.today()
                        models.storage.new(self)

        def __str__(self):
                """Shows string representation
                """
                Class = self.__class__.__name__
                MyPrint = ("[{}] ({}) {}".format(Class, self.id,
                                                 self.__dict__))
                return (MyPrint)

        def save(self):
                """Updates using updated_at
                """
                self.updated_at = datetime.today()
                models.storage.save()

        def to_dict(self):
                """Returns a Dictionary with all the key-values
                """
                Dict = self.__dict__.copy()
                Dict['__class__'] = str(type(self).__name__)
                Dict['created_at'] = self.created_at.isoformat()
                Dict['updated_at'] = self.updated_at.isoformat()
                return (Dict)
