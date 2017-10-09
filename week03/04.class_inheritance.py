class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        # is equal to:
        # super(Dog, self).__init__(name)
        self.__breed = breed

    def say(self):
        return f"{self.name}"

    def get_breed(self):
        return self.__breed


# class mix-ins
import json


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

# multiple class inheritance:
class ExDog(Dog, ExportJSON):
    def get_breed(self):
        return "Порода {0} - {1}".format(self.name, self.__breed)

# Linearisation of class inheritance
# MRO - method resolution order
# see __mro__ of class


# issubclass(subclass, class)
# isinstance(object, class)

# how to use a super() within multiple class inheritance:
class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = f"Шерстяная собака породы {breed}"


# class composition
