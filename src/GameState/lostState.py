from src.GameState.IState import IState

class LostState(IState):
    def process(self,game_play):
        print(f'You lose! The word was {game_play.word_to_guess}')
