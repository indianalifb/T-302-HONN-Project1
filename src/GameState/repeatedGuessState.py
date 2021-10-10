from src.GameState.IState import IState



class RepeatedGuessState(IState):
    #user guesses same letter again
    def process(self,letter, game_play):
        game_play.message = "You've repeated a guess!"
        game_play.set_state(game_play.get_holding_state())