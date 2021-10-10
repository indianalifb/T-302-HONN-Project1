# from src.GameMode.normal_gamemode import NormalGameMode
# from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.IGameMode import IGameMode
from src.reader import Reader
from src.GameState.correctGuessState import CorrectGuessState
from src.GameState.holdingState import HoldingState
from src.GameState.incorrectGuessState import IncorrectGuessState
from src.GameState.lostState import LostState
from src.GameState.repeatedGuessState import RepeatedGuessState
from src.GameState.wonState import WonState

CHAR_PLACEHOLDER = '-'


class GamePLay:
    def __init__(self, reader: Reader, won_state: WonState, repeated_guess_state: RepeatedGuessState, lost_state: LostState, incorrect_guess_state: IncorrectGuessState, holding_state: HoldingState, correct_guess_state: CorrectGuessState):
        self.won_state = won_state
        self.repeated_guess_state = repeated_guess_state
        self.lost_state = lost_state
        self.incorrect_guess_state = incorrect_guess_state
        self.holding_state = holding_state
        self.correct_guess_state = correct_guess_state
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
        self.message = ""
        self.reader = reader
        self.__state = holding_state
        self.letter_storage = []

    def get_won_state(self):
        return self.won_state

    def get_repeated_guess_state(self):
        return self.repeated_guess_state

    def get_lost_state(self):
        return self.lost_state

    def get_incorrect_guess_state(self):
        return self.incorrect_guess_state

    def get_holding_state(self):
        return self.holding_state

    def get_correct_guess_state(self):
        return self.correct_guess_state

    def set_state(self, state):
        self.__state = state

    def process(self, letter):
        """Requests the state to process the guessed letter.

        The State takes care of updating the lives, guessed_letters and providing a
        message for the gameplay"""
        self.__state.process(letter, self)
        self.__state.process(letter,self)

    def start_game(self):
        while self.number_of_guesses !=0:
            if self.__state == self.won_state:
                self.__state.process(self)
                return
            self.print_game_screen()
            letter = input('Guess a letter: ')
            self.process(letter)
            print('\n' + self.message + '\n')
        if self.__state == self.lost_state:
                self.__state.process(self)
                return



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
        self.start_game()

    def put_letter_in_word_in_hiding(self, user_guess):
        for i in range(0, len(self.word_to_guess)):
            if self.word_to_guess[i] == user_guess:
                my_list = []
                my_list[:0] = self.word_in_hiding
                my_list[i] = user_guess
                self.word_in_hiding = ''.join([str(elem) for elem in my_list])

    def won(self):
        print("IN WON")
        """Tests if all letters of in word are in guessed_letters"""
        return all(l in self.letter_storage for l in self.word_to_guess)


    def lost(self):
        """Tests if we have run out of lives"""
        return self.number_of_guesses <= 0




