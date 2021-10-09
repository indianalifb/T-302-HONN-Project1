import os
from src.hangman import Hangman
from src.db_connections.postgres_db_connection import PostgresDbConnection
from src.player import Player
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection
from src.infrastructure.container import Container
from src.Players.players_list import PlayersList
from src.infrastructure.settings import Settings
from src.db_connections.db_config import DbConfig

def run_migrations(db_connection: DbConnection):
    dir = './migrationsrcipts'
    for filename in os.listdir(dir):
        with open(f'{dir}/{filename}') as fileobj:
            db_connection.execute(fileobj.read())
        db_connection.commit()

def create_postgres_db_config(settings: Settings):

    return PostgresDbConnection(db_config=DbConfig(
        host=settings.postgres_log_host,
        user=settings.postgres_log_user,
        password=settings.postgres_log_password,
        database=settings.postgres_log_database
        ))

def start_game(hangman: Hangman):
    hangman.welcome_screen()



if __name__ == '__main__':
    container = Container()
    container.config.from_pydantic(Settings(_env_file='src/infrastructure/.env'))
    hangman = container.hangman()
    start_game(hangman)