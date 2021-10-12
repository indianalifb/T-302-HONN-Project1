from src.Observer.Observable import Observable
from src.Observer.Observer import Observer
from src.Repository.user_name_repository import UserNameRepository

class ObservableHighScoreConcrete (Observable):
    def __init__(self, repository: UserNameRepository):
        self.__high_score = None
        self.observers: list[Observer] = []
        self.repository = repository

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_new_high_score(self, high_score, username):
        if self.__high_score == None:
            self.__high_score = high_score
            self.repository.save_high_score(high_score, username)
            self.notify_observers()
        elif self.__high_score < high_score:
            self.__high_score = high_score
            self.repository.save_high_score(high_score, username)
            self.notify_observers()
        else:
            return

    def get_high_score(self):
        return self.__high_score