from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.IGameMode import IGameMode


class GamePLay:
    def _init__(self, game_mode: IGameMode):
        self.number_of_guesses = 0
        self.minus_points = 0
        self.total_points = 0
        if game_mode is not None:
            self.game_mode = game_mode


    def get_game_mode_elements(self):
        self.number_of_guesses = self.game_mode.nr_of_guesses()
        self.minus_points = self.game_mode.minus_points()
        self.total_points = self.game_mode.total_points()
    