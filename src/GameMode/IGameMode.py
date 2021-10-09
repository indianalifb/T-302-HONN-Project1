from abc import ABC, abstractmethod


class IGameMode(ABC):
    @abstractmethod
    def nr_of_guesses(self):
        pass


    @abstractmethod
    def minus_points(self):
        pass

    @abstractmethod
    def total_points(self):
        pass


