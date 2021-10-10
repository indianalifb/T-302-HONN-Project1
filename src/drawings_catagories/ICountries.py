from abc import ABC, abstractmethod


class ICountries(ABC):
    @abstractmethod
    def draw_countries(self):
        pass
    def print_countries(self, countries_list,number):
        for i in range(len(countries_list)):
            print(countries_list[number][i])
