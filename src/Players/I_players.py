from abc import ABC, abstractmethod


class IPlayers(ABC):
    @abstractmethod
    def add(self) -> None:
        pass

    @abstractmethod
    def lookup(self, name: str) -> str:
        pass
