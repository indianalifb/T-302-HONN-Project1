from abc import ABC, abstractmethod


class IFood(ABC):
    @abstractmethod
    def draw_food():
        pass
