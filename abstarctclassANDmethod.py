# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod


class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type = "rectanle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length* self.breadth

rect1 = rectangle()

print(rect1.printarea())
