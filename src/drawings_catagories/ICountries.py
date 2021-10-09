from abc import ABC, abstractmethod


class ICountries(ABC):
    @abstractmethod
    def draw_countries():
        pass
        
