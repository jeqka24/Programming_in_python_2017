# Metaclasses.
#  - Derived from type
#  - 1st parameter is class
#  - used as "class <ClassName>(metaclass=<metaclass_name>,<ParentClass>):"

class Class:
    pass
obj = Class()

parents = () # see MRO
attrs = {"luke":"You are the Chosen One!"} # attributes - see if this corresponds to __dict__

NewClass = type("NewClass", parents, attrs)

jedi = NewClass()

print(jedi.__dict__)

class Meta(type):
    def __new__(cls, name, parent, attrs):
        print("Creating - {}".format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parent, attrs)

    def __init__(cls, name, parent, attrs):
        print("Initializing - {}".format(name))

        if not hasattr(cls,'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, parent, attrs)

class Base(metaclass=Meta): pass

class A(Base): pass

class B(Base): pass

class C(A): pass

alice = A()
bob = B()
clive = C()


print(Base.registry)
print(A.registry)
print(B.registry)
print(C.registry)
print("="*78)
print(Base.__subclasses__())
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())
print("="*78)
print(alice.registry)
print(bob.registry)
print(clive.registry)
