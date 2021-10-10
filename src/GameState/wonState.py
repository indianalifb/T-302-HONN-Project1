from src.GameState.IState import IState



class WonState(IState):
    def process(self,game_play):
        print("You WON!")
        print(f'The word was indeed {game_play.word_to_guess}')