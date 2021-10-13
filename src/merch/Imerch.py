from abc import ABC, abstractmethod


class Imerch(ABC):

    @abstractmethod
    def getDescription(self):
        pass


    @abstractmethod
    def cost(self):
        pass
