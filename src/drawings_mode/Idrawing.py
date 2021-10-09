from abc import ABC, abstractmethod


class Idrawing(ABC):
    @abstractmethod
    def create_animal():
        pass


    @abstractmethod
    def create_food():
        pass

    @abstractmethod
    def create_country():
        pass

