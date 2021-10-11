from src.Repository.user_name_repository import UserNameRepository
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection

class FriendValidator:
    '''Validate that the friend is in the user's friend list'''
    def __init__(self, repo: UserNameRepository, connection: DbConnection, validator: UsernameValidator):
        self.__repo = repo(connection, validator)

    def validate(self, username: str, friend_username: str) -> bool:
        return self.__repo.are_friends(username, friend_username)
