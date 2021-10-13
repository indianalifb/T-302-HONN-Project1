from abc import ABC, abstractmethod


class Idrawing(ABC):
    @abstractmethod
    def create_animal(self):
        pass


    @abstractmethod
    def create_food(self):
        pass

    @abstractmethod
    def create_country(self):
        pass

