#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        state_id = ''
        name = ''
        super().__init__(self, *args, *kwargs)
