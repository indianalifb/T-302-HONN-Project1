from src.GameState.IState import IState


class IncorrectGuessState(IState):
    '''The user guessed incorrectly'''
    def process(self,letter, game_play):
        game_play.wrong_guess += 1
        game_play.number_of_guesses -= 1
        game_play.message = f"Incorrect guess! Minus {game_play.minus_points} points!. Score now:{game_play.total_points} points"
        game_play.total_points -= game_play.minus_points
        game_play.letter_storage.append(letter)
        if game_play.number_of_guesses == 0:
            game_play.set_state(game_play.get_lost_state())
        else:
            game_play.set_state(game_play.get_holding_state())