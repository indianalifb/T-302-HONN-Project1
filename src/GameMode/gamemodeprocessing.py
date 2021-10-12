from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.IGameMode import IGameMode
from src.GameMode.IgameModeCreator import IGamemodeCreator


class GamemodeProcessing(IGamemodeCreator):
    def __init__(self, normal_game_mode: NormalGameMode, competitive_game_mode: CompetitiveGameMode):
        self.game_modes = [normal_game_mode, competitive_game_mode]

    def factory_method(self, mode) -> IGameMode:
        if mode == 'n':
            return self.game_modes[0]
        else:
            return self.game_modes[1]