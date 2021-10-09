from typing import Optional
from src.db_connections.db_config import DbConfig
from src.Repository.db_connection import DbConnection
import psycopg2
from src.username_validator import UsernameValidator
from src.db_connections.postgres_db_connection import PostgresDbConnection

class UserNameRepository:
    def __init__(self, connection : DbConnection, validator :UsernameValidator):
        self.__connection = connection
        self.validator = validator

    def save_username(self, username):
        if self.validator:
            self.__connection.execute(
            f'''
            INSERT INTO player (username,highscore) VALUES ('{username}', {0})
            ''')
            self.__connection.commit()
        else:
            None

    def get_username(self, username):
        usernamedb = self.__connection.execute(f'''
        SELECT username FROM Player WHERE username = '{username}'
        ''')
        if len(usernamedb) == 0:    
            return None
        else:
            return usernamedb[0]







