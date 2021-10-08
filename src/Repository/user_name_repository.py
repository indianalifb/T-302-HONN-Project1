from db_connection import DbConnection
import psycopg2
import username_validator

class UserNameRepository:
    def __init__(self, connection: DbConnection, validator = username_validator):
        self.__connection = connection
        self.validator = validator

    def save_username(self, username):
        if self.validator:
            self.__connection.execute(
            "INSERT INTO Player (USERNAME) VALUES '{username}'")
            self.__connection.commit()
        else:
            None

    def get_username(self, username):
        usernamedb = self.__connection.execute(
        "SELECT username FROM Player WHERE username = '{username}'")
        if len(usernamedb) == 0:
            return None
        else:
            return usernamedb[0]





