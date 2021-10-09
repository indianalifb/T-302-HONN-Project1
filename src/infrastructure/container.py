from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from src.hangman import Hangman
from src.player import Player
from src.message_sender import MessageSender
from src.Players.players_list import PlayersList
from src.Repository.user_name_repository import UserNameRepository
from src.Repository.leader_board_repository import LeaderBoardRepository
from src.username_validator import UsernameValidator
from src.db_connections.db_config import DbConfig
from src.infrastructure.settings import Settings
from src.db_connections.postgres_db_connection import PostgresDbConnection

class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    postgres_db_config = providers.Singleton(
        DbConfig,
        host=config.postgres_log_host,
        user=config.postgres_log_user,
        database=config.postgres_log_database,
        password=config.postgres_log_password)

    db_connection_provider = providers.Selector(
        config.environment.value,
        prod=providers.Singleton(
            PostgresDbConnection, 
            db_config=postgres_db_config
        )
    )

    validator = providers.Singleton(
        UsernameValidator
    )

    repository = providers.Singleton(
        UserNameRepository,
        connection = db_connection_provider,
        validator = validator,
    )

    leaderboard = providers.Singleton(
            LeaderBoardRepository,
            connection = db_connection_provider
            )

    player_list = providers.Singleton(
        PlayersList,
        repository = repository,
        validator = validator,
    )

    message_sender = providers.Singleton(
        MessageSender,
    )


    player_provider = providers.Factory(
        Player,
        message_sender = message_sender,
        player_list = player_list
    )

    hangman = providers.Singleton(
        Hangman,
        player_list = player_list,
        leaderboard = leaderboard
    )
