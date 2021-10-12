from enum import Enum
from random import choice, randint
from src.readers.i_csv_reader import ICSVReader
from src.readers.i_txt_reader import ITXTReader
from src.readers.csv_reader_adapter import CSVReaderAdapter
import os

class Category(Enum):
    A = "Animals"
    C =  "Countries"
    F = "Food"

class Difficulty(Enum):
    E = "Easy"
    M = "Medium"
    H = "Hard"

class Reader():
    '''Reader takes no arguments to initialize'''

    def __init__(self, txtReader, adapter):
        self.txtReader = txtReader
        self.adapter = adapter

    def get_words(self, cat, diff):
        '''Call function with category letter for ex. "A" for animals,
            and difficulty letter ex. "m" for medium'''
        # If category chosen is random we chose a random category
        if cat == 'R':
            cat = choice(list(Category)).value
        else:
            cat = Category[cat.upper()].value

        diff = Difficulty[diff.upper()].value
        word_dir = "src/WordData/{}".format(cat)
        # try:
        for filename in os.listdir(word_dir):
            if filename[:len(diff)] == diff:
                if filename.endswith('.txt'):
                    words = self.txtReader.read_txt_file("{}/{}".format(word_dir,
                                                                       filename))
                else:
                    words = self.adapter.read_csv_file("{}/{}".format(word_dir,
                                                                     filename))
                return words[randint(0, len(words)-1)]

        # except FileNotFoundError:
            # print("File not found")
            # None
