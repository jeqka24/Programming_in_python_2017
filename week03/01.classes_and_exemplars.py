# Classes are named CamelCase
# functions are named snake_case

class Human:
#    def __del__(self):
#        print("Googbye!")
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age


class Robot:
    """Bite my shining ass!"""

# class exemplars are hashable!

class Planet:

    count = 1 # class method

    def __init__(self, name, population=None):
        print("init called!")
        # count is not initialized, so when accessing to .count,
        # first lookup is on exemplar, then - to the class
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __new__(cls, *args, **kwargs):
        print("new called!")
        obj = super().__new__(cls) # calling parent's object method __new__
        return obj

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

earth = Planet("Earth")
mars = Planet("Mars")

# Fuctions that operates in the context of exemplar

