#!/usr/bin/python3
""" command line cmd
"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage
import shlex
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class HBNB for command line CMD
    """
    prompt = '(hbnb) '
    ClassGroup = {"BaseModel": BaseModel, "User": User,
                  "State": State, "City": City, "Place": Place,
                  "Amenity": Amenity, "Review": Review}

    def do_EOF(self, line):
        """EOF command End Of File character """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        return False

    def do_help(self, line):
        """Help command shows info of each command"""
        cmd.Cmd.do_help(self, line)

    def do_create(self, line):
        """Creates new BaseModel's instance, saves to JSON file) N prints id.
Ex: $ create BaseModel
        """
        if line is None or line == '':
            print("** class name missing **")
        elif line not in self.ClassGroup:
            print("** class doesn't exist **")
        else:
            Instance = self.ClassGroup[line]()
            Instance.save()
            print(Instance.id)

    def do_show(self, line):
        """ Prints string repr. of instance based on class name-id.
Ex: $ show BaseModel 1234-1234-1234
        """
        if line is None or line == '':
            print("** class name missing **")
        else:
            Args = line.split(' ')
            if Args[0] not in self.ClassGroup:
                print("** class doesn't exist **")
            elif len(Args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(Args[0], Args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes instance based on class name-id and saves to Json File
Ex: $ destroy BaseModel 1234-1234-1234
        """
        if line is None or line == '':
            print("** class name missing **")
        else:
            Args = line.split(' ')
            if Args[0] not in self.ClassGroup:
                print("** class doesn't exist **")
            elif len(Args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(Args[0], Args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del(storage.all()[key])
                    storage.save()

    def do_all(self, line):
        """Prints all string repr of all instances based or not on class name.
Ex: $ all BaseModel or $ all
        """
        Objects = storage.all()
        if line != '':
            Args = line.split(' ')
            if Args[0] not in self.ClassGroup:
                print("** class doesn't exist **")
            else:
                Instance = [str(V) for K, V in Objects.items()
                            if type(V).__name__ == Args[0]]
                print(Instance)
        else:
            Instance = [str(V) for K, V in Objects.items()]
            print(Instance)

    def do_update(self, line):
        """Updates instance based on ClassName-Id adding/updating attribute.
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        Args = shlex.split(line)
        if len(Args) == 0:
            print("** class name missing **")
        elif len(Args) == 1:
            print("** instance id missing **")
        elif len(Args) == 2:
            print("** attribute name missing **")
        elif len(Args) == 3:
            print("** value missing **")
        elif Args[0] not in self.ClassGroup:
            print("** class doesn't exist **")
        else:
            Objects = storage.all()
            Key = Args[0] + '.' + Args[1]
            InstanceCheck = False
            for K, V in Objects.items():
                if K == Key:
                    InstanceCheck = True
                    Values = Objects.get(K)
                    setattr(V, Args[2], Args[3])
                    V.save()
            if InstanceCheck is False:
                print("** no instance found **")
    def strip_clean(self, line):
        """strips the args and return string
        """
        MyList = []
        MyList.append(line[0])
        try:
            Dict = eval(
                line[1][line[1].find('{'):line[1].find('}')+1])
        except Exception:
            Dict = None
        if isinstance(Dict, dict):
            String = line[1][line[1].find('(')+1:line[1].find(')')]
            MyList.append(((String.split(", "))[0]).strip('"'))
            MyList.append(Dict)
            return MyList
        String = line[1][line[1].find('(')+1:line[1].find(')')]
        MyList.append(" ".join(String.split(", ")))
        return " ".join(i for i in MyList)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        count = 0
        MyList = line.split('.')
        if len(MyList) >= 2:
            if MyList[1] == "all()":
                self.do_all(MyList[0])
            elif MyList[0]in self.ClassGroup and MyList[1] == "count()":
                if (MyList[0] not in self.ClassGroup):
                    print("** class doesn't exist **")
                    return (False)
                else:
                    for key in models.storage.all():
                        if key.startswith(MyList[0]):
                            count += 1
                    print(count)
            elif MyList[1][:4] == "show":
                self.do_show(self.strip_clean(MyList))
            elif MyList[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(MyList))
            elif MyList[1][:6] == "update":
                Args = self.strip_clean(MyList)
                if isinstance(Args, list):
                    obj = storage.all()
                    key = Args[0] + ' ' + Args[1]
                    for k, v in Args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(Args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
