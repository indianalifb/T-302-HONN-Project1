import random
import sys
import csv
import json

FILENAME = 'HangmanWords.txt'
CHAR_PLACEHOLDER = '-'


class Hangman:

    def __init__(self, guess_word=''):
        self.word_list = []
        self.guess_word = guess_word
        self.guess_word_size = 0
        self.num_guesses = 0
        self.num_wins = 0
        self.num_losses = 0
        self.playerName = ''
        self.score = 0

    def hangman_main_menu(self):
        print('-----Hangman-----')
        print('Start New Game = s')
        print('See History = h')
        print('Add a new word to guess = a')
        user_val = input('Input: ')
        if user_val == 's':
            self.playerName = input('Select a player name: ')
            self.initialize_game()
        elif user_val == 'h':
            print('\n')
            self.open_history_file()
            print('\nDo you want to go back to main menu or start a new game?')
            print('b = back to main menu   s = Start a new game')
            user_choice = input('Input: ')
            if user_choice == 'b':
                self.hangman_main_menu()
            else:
                self.playerName = input('Select a player name: ')
                self.initialize_game()
        elif user_val == 'a':
            new_word = input('Word to add: ').lower()
            self.write_in_words_file(new_word)
            print('Word added!')
            print('\nDo you want to go back to main menu or start a new game?')
            print('b = back to main menu   s = Start a new game')
            user_choice = input('Input: ')
            if user_choice == 'b':
                self.hangman_main_menu()
            else:
                self.playerName = input('Select a player name: ')
                self.initialize_game()

    def write_in_words_file(self, new_word):
        f = open("HangmanWords.txt", "a+")
        f.write("\n")
        f.write(new_word)
        f.close()

    def write_in_history_file(self):
        a_list = []
        a_list.append(str(self.playerName))
        a_list.append(str(self.num_wins))
        a_list.append(str(self.num_losses))
        a_list.append(str(self.score))
        string = ','.join(a_list)
        f = open("HangmanGameHistory.csv", "a+")
        f.write("\n")
        f.write(string)
        f.close()

    def open_words_file(self, FILENAME):
        file_object = open(FILENAME, 'r')
        for line in file_object:
            word = line.strip('\n')
            self.word_list.append(word)

    def open_history_file(self):
        with open('HangmanGameHistory.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(json.dumps(row).strip('{}'))

    def randomSeed(self):
        the_word = random.choice(self.word_list)
        self.guess_word = list(the_word)
        self.guess_word_size = len(the_word)

    def initialize_guess_word(self):
        guess_word_w_placeholder = [CHAR_PLACEHOLDER]*len(self.guess_word)
        return guess_word_w_placeholder

    def initialize_game(self):
        self.open_words_file(FILENAME)
        self.randomSeed()
        guess_word_w_placeholder = self.initialize_guess_word()
        self.print_instructions(guess_word_w_placeholder)

    def print_instructions(self, guess_word_w_placeholder):
        print('\n----New Game----')
        print('Player: {}'.format(self.playerName))
        print('word to guess: ', ''.join(self.guess_word))
        print('The word you need to guess has {} characters'.format(
            self.guess_word_size))
        print('You can guess the whole word or one letter at a time')
        user_num_guesses = int(input('Select number of guesses: '))
        while user_num_guesses < self.guess_word_size:
            print('\nPlease select a number bigger than {}'.format(
                self.guess_word_size))
            user_num_guesses = int(input('Select number of guesses: '))
        print('---------------------')
        self.num_guesses = user_num_guesses
        print('\nYou have {} guesses left!'. format(self.num_guesses))
        word_string = ''.join(guess_word_w_placeholder)
        print('Word to guess: {}'.format(word_string))
        self.play(guess_word_w_placeholder)

    def play(self, guess_word_w_placeholder):
        letter_storage = set()
        while self.num_guesses != 0:
            guess = input("\nWhat's your guess?: ").lower()
            the_guess = list(guess)
            if len(the_guess) == 1:
                if guess in letter_storage:
                    print('You already guessed that letter!')
                else:
                    letter_storage.add(guess)
                    if guess in self.guess_word:
                        self.score += 5
                        print('You guessed correctly!')
                        print('\n---------------------')
                        letter_index = [i for i, x in enumerate(
                            self.guess_word) if x == guess]
                        self.change_guess_word_w_placeholder(
                            guess_word_w_placeholder, guess, letter_index)
                        word_string = ''.join(guess_word_w_placeholder)
                        if not CHAR_PLACEHOLDER in guess_word_w_placeholder:
                            self.score += 30
                            self.won()
                        else:
                            print('\nYou have {} guesses left!'. format(
                                self.num_guesses))
                            print('Word to guess: {}'.format(word_string))
                    else:
                        print('letter not in word')
                        print('\n---------------------')
                        self.num_guesses -= 1
                        self.score -= 5
                        print('\nYou have {} guesses left!'. format(
                            self.num_guesses))
                        word_string = ''.join(guess_word_w_placeholder)
                        print('Word to guess: {}'.format(word_string))
            elif len(the_guess) == self.guess_word_size:
                self.guess_whole_word(the_guess, guess_word_w_placeholder)
            else:
                print('Please only write one letter at a time or the whole word that has {} characters'.format(
                    self.guess_word_size))
        else:
            self.lost()

    def guess_whole_word(self, the_guess, guess_word_w_placeholder):
        if the_guess == self.guess_word:
            self.score += 50
            self.won()
        else:
            print('Wrong word')
            self.num_guesses -= 1
            print('You have {} guesses left!'. format(
                self.num_guesses))
            word_string = ''.join(guess_word_w_placeholder)
            print('Word to guess: {}'.format(word_string))
            self.play(guess_word_w_placeholder)

    def won(self):
        self.num_wins += 1
        print('\nYOU WON!')
        word_string = ''.join(self.guess_word)
        print('The secret word was: {}'.format(word_string))
        if self.num_losses == 0:
            self.score += 20
        self.play_again()

    def lost(self):
        self.num_losses += 1
        print('GAME OVER - you lost')
        word_string = ''.join(self.guess_word)
        print('The secret word was: {}'.format(word_string))
        self.play_again()

    def change_guess_word_w_placeholder(self, guess_word_w_placeholder, guess, letter_index):
        for index in letter_index:
            guess_word_w_placeholder[index] = guess

    def play_again(self):
        print('\nDo you want to quit the game or start again?')
        print('q = quit   s = start again')
        user_input = input('I want to: ').lower()
        if user_input == 's':
            self.initialize_game()
        elif user_input == 'q':
            print('\nGame summary:')
            print('Player name: {}'.format(self.playerName))
            print('Number of wins: {}'.format(self.num_wins))
            print('Number of losses: {}'.format(self.num_losses))
            print('Total score: {}'.format(self.score))
            self.write_in_history_file()
            sys.exit('--Game exited--')


if __name__ == '__main__':
    h = Hangman()
    h.hangman_main_menu()
