from src.GameState.IState import IState



class WonState(IState):
    def process(self,game_play):
        game_play.message = f"!You WON! \nThe word was indeed {game_play.word_to_guess}"