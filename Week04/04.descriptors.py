class Descriptor:
    def __init__(self):
        pass

    def __set__(self, instance, value):
        print(f"Sef {instance} to {value}")


    def __get__(self, instance, owner):
        print(f"Get {instance} from {owner}")

    def __delete__(self, instance):
        print("Deleting {instance}")

class Class:
    descriptor = Descriptor()

instance = Class()


class ImportantValue:
    def __init__(self, amount = 0):
        self.amount = amount

    def __set__(self, instance, value):
        with open("log.txt","a") as f:
            f.write(str(value)+"\n")
        self.amount = value

    def __get__(self, instance, owner):
        return self.amount


class Account:
    amount = ImportantValue()
    def __init__(self, amount = 0):
        self.amount = amount

bobs_account = Account(100)
bobs_account.amount = 15
bobs_account.amount += 100

with open("log.txt","r") as f:
    print(f.read())


class User:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self):
        return "{first_name} {second_name}".format(**self.__dict__)

    @property
    def hello(self):
        return "Hello, I am {}".format(self.full_name)


amy = User("Amy", "Webber")
print(amy.full_name)
print(amy.hello)

# see Week03, methods

class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func

class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)

        def new_func(*args, **kwargs):
            return self.func(owner, *args, **kwargs)

        return new_func

class Class:
    @property
    def original(self):
        return "original"

    @Property
    def custom_sugar(self):
        return "custom sugar"

    def custom_pure(self):
        return "custom pure"

    custom_pure = Property(custom_pure)

obj = Class()
print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure)

# __slots__ - fixes a number of attributes - done via __set__/__get__ for __slots__
