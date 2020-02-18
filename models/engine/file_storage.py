#!/usr/bin/python3
"""json data format
"""
import models
import json


class FileStorage:
    """ serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        K = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[K] = obj

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
                objs = json.load(TheFile)
            for K, V in objs.items():
                self.__objects[K] = models.ClassGroup[V["__class__"]](**V)
        except:
            pass
