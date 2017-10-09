# @classmethod - makes method belongs to class, not a exemplar - First element is class, not a self
# @staticmethod - no-class, no-entity functions. Use it for scope
# property() - computational field. See class Robot.
# @property - get-only computational method.
# Also, see Week04\04.descriptors.py

class Human:
    def __init__(self, name, age = 0):
        self._name = name
        self._age = age

    # calling internal functions
    def _say(self, text):
        print(text)
    def say_name(self):
        self._say(f"Hello! I,m {self.name}.")
    def say_age(self):
        self._say(f"I am {self.age} years old.")
    @property
    def health(self, value=100):
        if value >= 100:print("Good health!")
        return value

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


class Robot:
    def __init__(self, power=0):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value >= 0:
            self._power = value
        else:
            self._power = 0

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("made robot useless")
        del self._power


class Planet:
    count = 0 # class method
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1 # counting total planet count
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def add_human(self, human):
        if isinstance(human, Human):
            print(f"Welcome to {self.name}, {human.name}!")
            self.population.append(human)