#!/usr/bin/python3
"""Init the File Storage System
"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine import file_storage

ClassGroup = {
    "BaseModel": BaseModel,
    "User": User, "State": State,
    "City": City, "Place": Place,
    "Amenity": Amenity, "Review": Review}

storage = file_storage.FileStorage()
storage.reload()
