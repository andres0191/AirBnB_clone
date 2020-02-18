#!/usr/bin/python3
"""inherits from base model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ list of string - empty list: it
        will be the list of Amenity.id later
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """Heritance mehtod since class  BaseModel"""
        super().__init__(self, *args, **kwargs)
