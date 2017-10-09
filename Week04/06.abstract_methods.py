from abc import ABCMeta, abstractmethod

class Sender(metaclass=ABCMeta):
    @abstractmethod   # this method must be overriden in child classes
    def send(self):
        pass

class PythonWay:
    def send(self):
        raise NotImplementedError

def Child(Sender):
    def send(self):
        return None

def PyChild(PythonWay):
    def send(self):
        return None