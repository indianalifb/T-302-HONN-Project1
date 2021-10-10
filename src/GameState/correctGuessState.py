from src.GameState.IState import IState



class CorrectGuessState(IState):
    def process(self, letter, game_play):
        print("CURRENT LETTER6:", letter)
        game_play.message = "Correct guess!"
        game_play.letter_storage.append(letter)
        game_play.put_letter_in_word_in_hiding(letter)
        if game_play.won():
            game_play.set_state(game_play.get_won_state())
        else:
            print("IN ELSE/CORRECT STATE")
            game_play.set_state(game_play.get_holding_state())