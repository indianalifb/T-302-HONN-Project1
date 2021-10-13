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

    '''Save the username to the database'''
    def save_username(self, username):
        if self.validator:
            self.__connection.execute(
            f'''
            INSERT INTO player (username,highscore) VALUES ('{username}', {0})
            ''')
            self.__connection.commit()
        else:
            None

    '''Get the username to the database'''
    def get_username(self, username):
        usernamedb = self.__connection.execute(f'''
        SELECT username FROM Player WHERE username = '{username}'
        ''')
        if len(usernamedb) == 0:
            return None
        else:
            return usernamedb[0]


    '''Check if the friend the user is trying to send a message to is the user's friend'''
    def are_friends(self, caller, friend):
        friends = self.__connection.execute(f'''
        SELECT adder_id, reciever_id FROM FRIENDS
        WHERE adder_id = (SELECT user_id FROM player WHERE username =
        '{caller}')
        AND
        reciever_id = (SELECT user_id FROM PLAYER WHERE USERNAME =
        '{friend}')
        ''')
        if len(friends) == 0:
            return False
        else:
            return True

    def save_high_score(self, high_score, username):
        self.__connection.execute(
        f'''
        UPDATE player SET highscore = '{high_score}' WHERE username = '{username}'
        ''')
        self.__connection.commit()

    def add_friend(self, adder, reciever):
        self.__connection.execute(f'''
                                  INSERT INTO FRIENDS(adder_id, reciever_id)
                                  VALUES
                                  ((SELECT USER_ID FROM PLAYER WHERE USERNAME = '{adder}'),
                                   (SELECT USER_ID FROM PLAYER WHERE USERNAME = '{reciever}'))
                                  ''')
