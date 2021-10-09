from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.IGameMode import IGameMode
from src.reader import Reader


class GamePLay:
    def __init__(self, reader: Reader):
        self.number_of_guesses = 0
        self.minus_points = 0
        self.total_points = 0
        self.word_to_guess = ""
        self.word_in_hiding = ""
        self.game_category = ""
        self.game_difficulty = ""
        self.game_mode = ""
        self.reader = Reader()



    def get_game_mode_elements(self):
        self.number_of_guesses = self.game_mode.nr_of_guesses()
        self.minus_points = self.game_mode.minus_points()
        self.total_points = self.game_mode.total_points()
        print("self.number_of_guesses:", self.number_of_guesses)
        print("self.minus_points:", self.minus_points)
        print("self.total_points:", self.total_points)
    

    def print_game_screen(self):
        print('-------------------------------------------------------')
        print("                     Guess The WORD!                   ")
        print("**                ",self.word_in_hiding,"            **")
        print('-------------------------------------------------------')
        #call print(drawing)

    
    def get_word(self):
        self.word_to_guess = self.reader.get_words(self.game_category, self.game_difficulty)
        word_len = len(self.word_to_guess)
        self.word_in_hiding = word_len * "_"
        print("word to guess:", self.word_to_guess)

    def placeholder_changes(self):
        pass

    def play(self, game_mode: IGameMode = None, difficulty = None, categegory = None):
        self.game_mode = game_mode
        self.game_difficulty = difficulty
        self.game_category = categegory
        print("self.game_mode:", self.game_mode)
        print("self.game_difficulty:", self.game_difficulty)
        print("self.game_category:", self.game_category)
        self.get_game_mode_elements()
        self.get_word()
        self.print_game_screen()
        user_guess = input("Guess a letter or the word!:")
        if len(user_guess) == 1:
            #hann er að giska a einn staf
            pass
        else:
            #hann er að giska á allt orðið
            pass

