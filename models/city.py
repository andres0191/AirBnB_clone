#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """ City (models/city.py):
        Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """Heritance mehtod since class  BaseModel"""
        super().__init__(self, *args, **kwargs)
