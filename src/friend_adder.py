from src.Repository.user_name_repository import UserNameRepository
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection

class FriendAdder:
    '''Creates a friend relationship between player A and player B'''
    def __init__(self, repo: UserNameRepository, connection: DbConnection,
                 validator: UsernameValidator):
        self.__repo = repo(connection, validator)

    def add_friend(self, adder: str, reciever: str) -> None:
        self.__repo.add_friend(adder, reciever)





