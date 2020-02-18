#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Heritance mehtod since class  BaseModel"""
        super().__init__(self, *args, **kwargs)
