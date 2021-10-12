from src.Players.I_players import IPlayers
from src.Repository.user_name_repository import UserNameRepository
from src.username_validator import UsernameValidator


class PlayersList(IPlayers):
    def __init__(self, repository : UserNameRepository, validator: UsernameValidator):
        self.repository = repository
        self.validator = validator

    def add(self, name):
        if self.validator:
            self.repository.save_username(name)
            return True
        else:
            return False

    def lookup(self, name: str) -> str:
        validate_username = self.repository.get_username(name)
        if validate_username == None:
            return False
        else:
            return True

    def add_high_score(self, name, highscore):
        self.repository.save_high_score(highscore,name)
