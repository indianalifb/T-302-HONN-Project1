from src.GameState.IState import IState



class RepeatedGuessState(IState):
    '''user guesses same letter again'''
    def process(self,letter, game_play):
        game_play.number_of_guesses -= 1
        game_play.message = f"You've repeated a guess! Already guessed the letter {letter}"
        game_play.set_state(game_play.get_holding_state())