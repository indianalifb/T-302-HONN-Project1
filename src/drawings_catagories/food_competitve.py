from src.drawings_catagories.IFood import IFood
from colorama import init
from colorama import Fore, Back, Style

class FoodCompetitive(IFood):
    def draw_food(self, number):
        food_list = [
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /|         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /|\        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /|\        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /          |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"         +---------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         O         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /|\        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         |         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        / \        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"==================" + Fore.BLUE +"               #"],
        ]
            
        self.print_food(food_list, number-1)

    def print_food(self, food_list, number):
        for i in range(len(food_list)):
            print(food_list[number][i])