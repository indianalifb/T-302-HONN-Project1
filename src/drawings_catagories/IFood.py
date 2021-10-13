from abc import ABC, abstractmethod


class IFood(ABC):
    @abstractmethod
    def draw_food(self, number):
        pass
    def print_food(self, food_list, number):
        for i in range(len(food_list)):
            print(food_list[number][i])