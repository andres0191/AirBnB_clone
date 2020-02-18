#!/usr/bin/python3
"""inherits from base model
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State (models/state.py):
        Public class attributes:
        name: string - empty strin
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """Heritance mehtod since class  BaseModel"""
        super().__init__(self, *args, **kwargs)
