from src.GameState.IState import IState
class HoldingState(IState):
    '''state that calculates the next state'''
    def process(self, guess, game_play):
        game_play.number_of_guesses -= 1
        if guess in game_play.letter_storage:
            game_play.set_state(game_play.get_repeated_guess_state())
        elif guess in game_play.word_to_guess:
            game_play.set_state(game_play.get_correct_guess_state())
        else:
            game_play.set_state(game_play.get_incorrect_guess_state())