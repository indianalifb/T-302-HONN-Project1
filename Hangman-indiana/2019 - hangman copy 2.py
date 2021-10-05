import random

# Constants to be used in the implementation
WORD_LIST = ["lion", "umbrella", "window", "computer", "glass", "juice",
             "chair", "desktop", "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'


def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)


def random_choice(WORD_LIST):
    the_word = random.choice(WORD_LIST)
    return the_word


def initialize_guess_word(the_word):
    guess_word = [CHAR_PLACEHOLDER]*len(the_word)
    return guess_word


def print_istructions(guess_word_w_placeholder):
    print('The word you need to guess has {} characters'.format(
        len(guess_word_w_placeholder)))
    word_string = ' '.join(guess_word_w_placeholder)
    print('Word to guess: {}'.format(word_string))


def play(the_word, guess_word_w_placeholder):
    letter_storage = set()
    num_guesses = 0
    while num_guesses < MAX_GUESS:
        guess = input("Choose a letter: ").lower()
        num_guesses = guessing_letters(
            guess, num_guesses, the_word, guess_word_w_placeholder, letter_storage)
        if not CHAR_PLACEHOLDER in guess_word_w_placeholder:
            print('You won!')
            print_current_guess_word(guess_word_w_placeholder)
            break
        else:
            print('You are on guess {}/{}'.format(num_guesses, MAX_GUESS))
            print_current_guess_word(guess_word_w_placeholder)
    else:
        print("You lost! The secret word was {}".format(the_word))


def guessing_letters(guess, num_guesses, the_word, guess_word_w_placeholder, letter_storage):
    if guess in letter_storage:
        print('You have already guessed that letter!')
    else:
        letter_storage.add(guess)
        num_guesses += 1
        if guess in the_word:
            print('You guessed correctly!')
        for i in range(0, len(the_word)):
            if the_word[i] == guess:
                guess_word_w_placeholder[i] = guess
            else:
                print('The letter is not in the word!')
    return num_guesses


def main():
    random_seed()
    the_word = random_choice(WORD_LIST)
    guess_word_w_placeholder = initialize_guess_word(the_word)
    print_istructions(guess_word_w_placeholder)
    play(the_word, guess_word_w_placeholder)


main()
