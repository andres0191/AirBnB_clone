#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import models
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_EOF(self, line):
        print()
        return True
    def do_quit(self, line):
        return True
    def emptyline(self):
        return False
    def do_help(self, line):
        cmd.Cmd.do_help(self, line)
    def do_create(self, line):
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
        if len(line) == 0:
            print("**  class name missing **")
            return
        objects = storage.all()
        line = line.split(" ")
        if len(line) < 2:
            print("** class doesn't exist **")
            return
        for key, value in objects.items():
            delim = key.split(".")
            if line[0] == delim[0] and line[1] == delim[1]:
                print(value)
                return
        print("** class doesn't exist **")
        return

    def do_destroy(self, line):
        pass
        
    def do_all(self, line):
        if line not in globals():
            print("** class doesn't exist **")
            return
        if len(line) > 0:
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