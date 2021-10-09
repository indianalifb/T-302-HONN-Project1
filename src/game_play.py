from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.IGameMode import IGameMode
from src.reader import Reader

CHAR_PLACEHOLDER = '-'


class GamePLay:
    def __init__(self, reader: Reader):
        self.number_of_guesses = 0
        self.number_of_wrong_guesses = 0
        self.minus_points = 0
        self.total_points = 0
        self.word_to_guess = ""
        self.word_in_hiding = ""
        self.game_category = ""
        self.game_difficulty = ""
        self.game_mode = ""
        self.guess = ""
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
        print("                     Guess The WORD!      guesses:",self.number_of_guesses ,"             ")
        print("**                     ",self.word_in_hiding,"                  **")
        print('-------------------------------------------------------')
        #call print(drawing), þarf að fa inn hversu mörg vitlaust eru komin

    
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
        self.play_game()


    def won(self):
        print("-----------------YOU WON!-----------------")
        print("TOTAL SCORE:", self.total_points)


    def lost(self):
        pass

    def play_game(self):
        self.print_game_screen()
        letter_storage = set()
        while self.number_of_guesses !=0:
            user_guess = input("Guess a letter or the word!:")
            the_guess = list(user_guess)
            if len(the_guess) == 1:
                if user_guess in letter_storage:
                    print('You already guessed that letter!')
                else:
                    letter_storage.add(user_guess)
                    if user_guess in self.word_to_guess:
                        print('You guessed correctly!')
                        print('\n-------------------------------------------------------')
                        for i in range(0, len(self.word_to_guess)):
                            if self.word_to_guess[i] == user_guess:
                                my_list = []
                                my_list[:0] = self.word_in_hiding
                                my_list[i] = user_guess
                                self.word_in_hiding = ''.join([str(elem) for elem in my_list])
                        print("self.word_in_hiding", self.word_in_hiding)
                        if '_' in self.word_in_hiding:
                            self.number_of_guesses -= 1
                            self.print_game_screen()
                        else:
                            #self.total_points += 30 get more point for winning?
                            self.won()
                            break
                    else:
                        print('letter not in word')
                        print('\n-------------------------------------------------------')
                        self.number_of_guesses -= 1
                        self.total_points -= self.minus_points
                        self.print_game_screen()
                #hann er að giska a einn staf
                pass
            else:
                #hann er að giska á allt orðið
                pass


