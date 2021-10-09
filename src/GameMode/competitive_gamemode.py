from src.GameMode.IGameMode import IGameMode

class CompetitiveGameMode(IGameMode):
    def nr_of_guesses(self):
        return 7

    def minus_points(self):
        return 30

    def total_points(self):
        return 210
