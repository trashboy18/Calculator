from abc import ABC,abstractmethod

class Operator(ABC):

    @abstractmethod
    def getSymbol(self):
        ...
    @abstractmethod
    def getPosition(self):
        ...
    @abstractmethod
    def getPriority(self):
        ...
    @abstractmethod
    def operate(self):
        ...




