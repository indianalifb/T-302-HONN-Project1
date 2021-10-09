from abc import ABC, abstractmethod


class IAnimal(ABC):
    @abstractmethod
    def draw_animal():
        pass
