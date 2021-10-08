from db_connection import DbConnection
import psycopg2

class UserNameRepository:
    def __init__(self, connection: DbConnection):
        self.__connection = connection

    def save_username(self, username):
        self.__connection.execute(
        "INSERT INTO Player (USERNAME) VALUES '{username}'")
        self.__connection.commit()

    def get_username(self, username):
        usernamedb = self.__connection.execute(
        "SELECT username FROM Player WHERE username = '{username}'")
        if len(usernamedb) == 0:
            return None
        else:
            return usernamedb[0]





