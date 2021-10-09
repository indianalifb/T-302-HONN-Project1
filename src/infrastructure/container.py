from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from player import Player
from message_sender import MessageSender
from Players.players_list import PlayersList
from Repository.user_name_repository import UserNameRepository
from username_validator import UsernameValidator
from db_connections.db_config import DbConfig
from infrastructure.settings import Settings
from db_connections.postgres_db_connection import PostgresDbConnection

class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    postgres_db_config = providers.Singleton(
        DbConfig,
        host=config.posgres_log_host,
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

    username_validator = providers.Singleton(
        UsernameValidator
    )

    username_repository = providers.Singleton(
        UserNameRepository,
        connection = db_connection_provider
    )


    player_list = providers.Singleton(
        PlayersList,
        username_repository = username_repository,
        validator = username_validator,
    )

    message_sender = providers.Singleton(
        MessageSender,
    )


    player_provider = providers.Factory(
        Player,
        message_sender = message_sender,
        player_list = player_list
    )