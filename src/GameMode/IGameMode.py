from abc import ABC, abstractmethod


class IGameMode(ABC):
    @abstractmethod
    def nr_of_guesses():
        pass


    @abstractmethod
    def minus_points():
        pass

    @abstractmethod
    def total_points():
        pass


