
from src.drawings_catagories.IAnimal import IAnimal
from colorama import init
from colorama import Fore, Back, Style

class AnimalNormal(IAnimal):
    def draw_animal(self, number):
        animal_list = [
            [Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                    " + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +"                   +" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-----------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \              |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__           |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o      |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o      |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         /         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /          |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"       w           |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o      |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         /\        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /(_)       |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"       w           |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o   (  |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)    __) |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         /\   (    |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /(_)___)   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"       w           |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o   (  |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)    __) |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         /\   (    |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /(_)___)   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"       w /         |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        |          |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        m          |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
            [Fore.BLUE + "#              "+ Fore.WHITE +" +-w---------------+" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"    \  c(..)o   (  |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"     \__(-)    __) |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"         /\   (    |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        /(_)___)   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"       w /|        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        | \        |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"        m  m       |" + Fore.BLUE +"               #",
            Fore.BLUE + "#              "+ Fore.WHITE +"                   |" + Fore.BLUE +"               #",
            Fore.BLUE + "#               "+ Fore.WHITE +"===================" + Fore.BLUE +"               #"],
        ]
            
        self.print_animal(animal_list,number-1)

    def print_animal(self, animal_list,number):
        for i in range(len(animal_list)):
            print(animal_list[number][i])
    

# new_s = AnimalNormal()
# new_s.draw_animal(0)
# print()
# new_s.draw_animal(1)
# print()
# new_s.draw_animal(2)
# print()
# new_s.draw_animal(3)
# print()
# new_s.draw_animal(4)
# print()
# new_s.draw_animal(5)
# print()
# new_s.draw_animal(6)
# print()
# new_s.draw_animal(7)
# print()
# new_s.draw_animal(8)
# print()
# new_s.draw_animal(9)





