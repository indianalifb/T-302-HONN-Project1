from abc import ABC, abstractmethod


class IAnimal(ABC):
    @abstractmethod
    def draw_animal(self):
        pass
    def print_animal(self, animal_list,number):
        for i in range(len(animal_list)):
            print(animal_list[number][i])