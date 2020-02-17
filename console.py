#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """Interpreter of commands"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """exit the program"""
        print()
        return True

    def do_quit(self, line):
        """exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        return False

    def do_help(self, line):
        """ (this action is provided by default by cmd
            but you should keep it updated and documented)
        """
        cmd.Cmd.do_help(self, line)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        print(line)
        if len(line) == 0:
            print("**  class name missing **")
            return
        if line in globals():
            instance = globals()[line]
            new_object = instance()
            print(new_object.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on
            the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        if len(line) == 0:
            print("**  class name missing **")
            return
        objects = storage.all()
        line = line.split(" ")
        print(line[0])
        if line[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        for key, value in objects.items():
            delim = key.split(".")
            if line[0] == delim[0] and line[1] == delim[1]:
                print(value)
                return
        print("** no instance found **")
        return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234.
        """
        pass

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name. Ex: $ all BaseModel or $ all.
        """
        if len(line) > 0:
            if line not in globals():
                print("** class doesn't exist **")
                return
            if line in globals():
                objects = storage.all()
            for key, value in objects.items():
                delim = key.split(".")
                if line == delim[0]:
                    print(value)
        else:
            obj = storage.all()
            for key, value in obj.items():
                print(value)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
