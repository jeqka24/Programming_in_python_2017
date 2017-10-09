import json


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


# prototype only class
class PetExport:
    def export(self, pet):
        raise NotImplementedError


class ExportJSON(PetExport):
    def export(self, pet):
        return json.dumps({
            "name": pet.name,
            "breed": pet.get_breed()
        }, ensure_ascii=False)


class ExportXML(PetExport):
    def export(self, pet):
        return """<?xml version="1.0" encoding="utf-8"?>
<dog>
<name>{0}</name>
<breed>{1}</breed>
</dog>
""".format(pet.name, pet.get_breed())


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()
        if not (isinstance(self._exporter, PetExport)):
            raise ValueError("Bad Exporter", exporter)

    def export(self):
        return self._exporter.export(self)


dog1 = ExDog("Шарик", "Дворняга", exporter=ExportJSON())
print(dog1.export())

dog1._exporter = ExportXML()
print(dog1.export())

dog2 = ExDog("Барбос", "Другая дворняга")
print(dog2.export())
