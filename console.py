#!/usr/bin/python3

from models.base_model import BaseModel
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
