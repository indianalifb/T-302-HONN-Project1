from src.GameMode.IGameMode import IGameMode

class NormalGameMode(IGameMode):
    def nr_of_guesses(self):
        return 10

    def minus_points(self):
        return 10

    def total_points(self):
        return 100
