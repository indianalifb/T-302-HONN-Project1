from src.Observer.Observer import Observer
from src.Observer.Observable import Observable
from src.Observer.IDisplayHighScore import IDisplayHighScore


class HighscoreDisplay(Observer, IDisplayHighScore):
    __high_score: int = None

    def update(self, observable: Observable):
        high_score_data = observable.get_high_score()
        self.__high_score = high_score_data
        self.display()

    def display(self):
        print(f"!NEW High Score! {self.__high_score}")
