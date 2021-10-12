from abc import ABC, abstractmethod


class IDisplayHighScore(ABC):
    @abstractmethod
    def display(self) -> None:
        pass