#!/usr/bin/python3
"""inherits from base model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Heritance mehtod since class  BaseModel"""
        super().__init__(self, *args, **kwargs)
