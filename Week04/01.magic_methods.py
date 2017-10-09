# 01. __init__

# 02. __new__

class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

a = Singleton()
b = Singleton()
a == b

# 03. __del__ - DO NOT TOUCH!

# 04. __str__ - used in print()

# 05. __hash__, __eq__

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):     # also used in dict
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email

# 06. __getattr__       - used when attribute not found
#     __getattribute__  - always used
#     __setattr__       - when trying to set attribute
#     __delattr__       - when trying to delete an attribute or method from object
class Researcher:
    def __getattr__(self, item):
        return "Not found"

    def __getattribute__(self, item):
        print("Looking for {item}".format(item=item))
        return object.__getattribute__(self, name)

obj = Researcher()
print(obj.attr)
print(obj.method)
print(obj.ASDLKFJ09GN)

class Ignorant:
    def __setattr__(self, key, value):
        print("Not going to set {} to {}".format(key, value))
    def __setattribute__

obj = Ignorant()
obj.math = True

# 07. __call__

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        with open(self.filename, "w") as f:
            f.write("Oh, Danny boy!...")
        return func

logger = Logger("log.txt")

@logger
def completely_useless_func():
    pass

# 08. __add__
#     __sub__
#     __div__
#     __mul__
#     __shl__
#     __shr__
#  remember the assotiativity of operations

# 09. __getitem__ - returns obj[key]
#     __setitem__ - sets obj[key]
class WordCounter:
    def __init__(self):
        self.__lst = {}

    def __setitem__(self, key, value):
        if self.__lst[key]:
            self.__lst[key] += 1
        else:
            self.__lst[key] = 1

    def __getitem__(self, item):
        return self.__lst[item]
