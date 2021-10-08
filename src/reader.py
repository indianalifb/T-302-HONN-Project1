from enum import Enum
from random import choice, randint

class Category(Enum):
    A = "Animals"
    C =  "Countries"
    F = "Food"

class Difficulty(Enum):
    E = "Easy"
    M = "Medium"
    H = "Hard"

class Reader:
    '''Reader takes no arguments to initialize'''

    def get_words(self, cat, diff):
        '''Call function with category letter for ex. "A" for animals,
            and difficulty letter ex. "m" for medium'''
       # If category chosen is random we chose a random category
       if cat == 'R':
            cat = choice(list(Category)).value
        else:
            cat = Category[cat.upper()].value
       

        diff = Difficulty[diff.upper()].value

        filename = "WordData/{}/{}{}.txt".format(cat, diff, cat.lower())

        try:
            with open(filename, 'r') as f:
                words = [line.strip() for line in f]
            
            return words[randint(0, len(words))]
        except FileNotFoundError:
            print("File not found") 
            None

if __name__ == "__main__":
    read = Reader()
    word = read.get_words("a", "m")
    print(word)
