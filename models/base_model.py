#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
	def __init__(self, *args, **kwargs):
		if kwargs != {} and kwargs is not None:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
				if key != "__class__":
					setattr(self, key, value)
		else:
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime.datetime.today()
                        self.updated_at = datetime.datetime.today()
                        models.storage.new(self)

	def __str__(self):
		MyClass = self.__class__.__name__
		MyPrint = ("[{}] ({}) {}".format(MyClass, self.id, self.__dict__))
		return (MyPrint)

	def save(self):
                self.updated_at = datetime.datetime.today()
                models.storage.save()

	def to_dict(self):
		Dict = self.__dict__.copy()
		Dict['__class__'] = str(type(self).__name__)
		Dict['created_at'] = self.created_at.isoformat()
		Dict['updated_at'] = self.updated_at.isoformat()
		return (Dict)
