from abc import ABC, abstractmethod


class IPlayers(ABC):
    @abstractmethod
    def add(self, name: str) -> bool:
        pass

    @abstractmethod
    def lookup(self, name: str) -> str:
        pass
