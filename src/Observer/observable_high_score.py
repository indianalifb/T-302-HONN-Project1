from src.Observer.Observable import Observable
from src.Observer.Observer import Observer

class ObservableHighScoreConcrete (Observable):
    __high_score = None
    observers: list[Observer] = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_new_high_score(self, high_score):
        if self.__high_score == None:
            self.__high_score = high_score
            self.notify_observers()
        elif self.__high_score < high_score:
            self.__high_score = high_score
            self.notify_observers()
        else:
            return

    def get_high_score(self):
        return self.__high_score