#!/usr/bin/python3

import models
import json


class FileStorage:
    """ serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        self.__objects["{}.{}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """Serialize __objects to Json File
        """
        NewDict = {}
        for id, values in self.__objects.items():
            NewDict[id] = values.to_dict()
        with open(self.__file_path, mode='w', encoding='UTF-8') as TheFile:
            json.dump(NewDict, TheFile)

    def reload(self):
        """Deserialize Json File to __objects
        """
        try:
            with open(self.__file_path, encoding='UTF-8') as TheFile:
                obj = json.load(TheFile)
            for K, V in obj.items():
                self.__objects[K] = models.ClassGroup[V["__class__"]](**V)
        except:
            pass
