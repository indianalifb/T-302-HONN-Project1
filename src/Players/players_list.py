from src.Players.I_players import IPlayers
from Repository.user_name_repository import UserNameRepository
import username_validator


class PlayersList(IPlayers):
    def __init__(self, repository : UserNameRepository, validator: username_validator):
        self.repository = repository
        self.validator = validator

    def add(self, name):
        if self.validator:
            self.repository.save_username(name)
        else:
            return None

    def lookup(self, name: str) -> str:
        validate_username = UserNameRepository.get_username(name)
        if validate_username == None:
            return False
        else:
            return True
