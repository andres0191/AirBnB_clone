# AirBnB clone - The console


![alt tag](https://camo.githubusercontent.com/8d76bb2b9f2eeeb22ba9236805e758b58eb7fdc4/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

In AirBnB clone: ​​the console is designed to make a clone of the airbnb platform where the user has the possibility to make a reservation of the hostel or room for the next vacation anywhere in the world. the first step is the console.

This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

**Each task is linked and will help you to:**

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. 
In our case, we want to be able to manage the **objects of our project:**

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
## Support for line-oriented command interpreters

**The objectives are:**

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

**Concepts:**

## CMD

The **Cmd** class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface. A Cmd instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate Cmd itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit Cmd‘s methods and encapsulate action methods. The optional argument completekey is the readline name of a completion key; it defaults to Tab. If completekey is not None and readline is available, command completion is done automatically. The optional arguments stdin and stdout specify the input and output file objects that the Cmd instance or subclass instance will use for input and output. If not specified, they will default to sys.stdin and sys.stdout. If you want a given stdin to be used, make sure to set the instance’s use_rawinput attribute to False, otherwise stdin will be ignored.

## UUID
The **UUID** provides immutable UUID objects (the UUID class) and the functions uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5 UUIDs as specified in RFC 4122. If all you want is a unique ID, you should probably call uuid1() or uuid4(). Note that uuid1() may compromise privacy since it creates a UUID containing the computer’s network address. uuid4() creates a random UUID.

**uuid.getnode()**
Get the hardware address as a 48-bit positive integer. The first time this runs, it may launch a separate program, which could be quite slow. If all attempts to obtain the hardware address fail, we choose a random 48-bit number with its eighth bit set to 1 as recommended in RFC 4122. “Hardware address” means the MAC address of a network interface, and on a machine with multiple network interfaces the MAC address of any one of them may be returned.

**uuid.uuid1(node=None, clock_seq=None)**
Generate a UUID from a host ID, sequence number, and the current time. If node is not given, getnode() is used to obtain the hardware address. If clock_seq is given, it is used as the sequence number; otherwise a random 14-bit sequence number is chosen.

**uuid.uuid3(namespace, name)**
Generate a UUID based on the MD5 hash of a namespace identifier (which is a UUID) and a name (which is a string).

**uuid.uuid4()**
Generate a random UUID.

**uuid.uuid5(namespace, name)**
Generate a UUID based on the SHA-1 hash of a namespace identifier (which is a UUID) and a name (which is a string).

The uuid module defines the following namespace identifiers for use with **uuid3()** or **uuid5()**.

# Magic Methods used in this proyect:

## **__init__**

The **__init__** method is a special method of a class in Python. The fundamental objective of the __init__ method is to initialize the attributes of the object we create.

The advantages of implementing the __init__ method instead of the initialize method are:

The **__init__** method is the first method that is executed when an object is created.
The **__init__** method is called automatically. In other words, it is impossible to forget to call it since it will be called automatically.
Who uses POO in Python (Object Oriented Programming) knows the purpose of this method.
Other features of the **__init__** method are:

It is executed immediately after creating an object.
The **__init__** method cannot return data.
The **__init__** method can receive parameters that are normally used to initialize attributes.
The **__init__** method is an optional method, however it is very common to declare it.

-Example:

```
class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"
```

## **__str__**

**__str__** is the function built into python, used to represent strings of objects. **__repr__** is another built-in that is similar to **__str__**. ... That method returns a printable string that represents that object, that is, what you will get when you print that object.

-Example:

```
class Foo():
    def __init__(self):
        self.l = [{"Susan": ("Boyle", 50, "alive")}, {"Albert": ("Speer", 106, "dead")}]
    def __str__(self):
        ret_str = ""
        for d in self.l:
            for k in d:
                ret_str += "".join([k, " ", d[k][0], " is ", str(d[k][1]), " and ", d[k][2], ". "])
        return ret_str
 
foo = Foo()
print (foo)
```
## ARGS, KWARGS

***args** and ****kwargs** are mostly used in function definitions. ***args** and ****kwargs** allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords. ***args** is used to send a non-keyworded variable length argument list to the function. Here’s an example to help you get a clear idea:

-Example:

```
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')
```

This produces the following result:

```
first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test
```

Our CMD is configured to recognize commands such as show, create, destroy, update, all and execute each of these commands respectively

**show:** Prints the string representation of an instance based on the class name and id. 
-Example:
```
$ show BaseModel 1234-1234-1234.
```

**create:** Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
-Example:
```
$ create BaseModel
```

**destroy:** Deletes an instance based on the class name and id (save the change into the JSON file).
-Example:
```
$ destroy BaseModel 1234-1234-1234.
```

**update:** Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
-Example:
```
$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
```

**all:** Prints all string representation of all instances based or not on the class name.
-Example:
```
$ all BaseModel or $ all.
```

**Authors:** 
-JOSE DIAZ [GitHub Perfil](https://github.com/jhosep7).
-ANDRES F. GARCIA R. [GitHub Perfil](https://github.com/andres0191).
