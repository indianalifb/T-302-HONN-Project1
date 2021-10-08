from src.exceptions.invalid_number_exception import InvalidNumberException
from src.Players.I_players import IPlayers
from Repository.user_name_repository import UserNameRepository


class PlayersList(IPlayers):
    def __init__(self, repository : UserNameRepository ):
        self.repository = repository

    def add(self, name):
        self.repository.save_username(name)

    def lookup(self, name: str) -> str:
        self.repository.get_username(name)
