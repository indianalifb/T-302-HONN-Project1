from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide, provided
from src.buy_merch import BuyMerch
from src.merch.Imerch import Imerch
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
from src.game_play import GamePLay
from src.reader import Difficulty, Reader
from src.game_play import GamePLay
from src.GameMode.normal_gamemode import NormalGameMode
from src.GameState.correctGuessState import CorrectGuessState
from src.GameState.holdingState import HoldingState
from src.GameState.incorrectGuessState import IncorrectGuessState
from src.GameState.lostState import LostState
from src.GameState.repeatedGuessState import RepeatedGuessState
from src.GameState.wonState import WonState
from src.friend_validator import FriendValidator
from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.GameMode.gamemodeprocessing import GamemodeProcessing
from src.Observer.observable_high_score import ObservableHighScoreConcrete
from src.Observer.HighscoreDisplay import HighscoreDisplay


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

    friend_validator = providers.Singleton(
        FriendValidator,
        repo = UserNameRepository,
        connection=db_connection_provider,
        validator=validator
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


    reader = providers.Singleton(
        Reader,
    )

    correct_guess_state = providers.Singleton(
        CorrectGuessState,
    )

    holding_state = providers.Singleton(
        HoldingState,
    )

    incorrect_guess_state = providers.Singleton(
        IncorrectGuessState,
    )

    lost_state = providers.Singleton(
        LostState,
    )

    repeated_guess_state = providers.Singleton(
        RepeatedGuessState,
    )

    won_state = providers.Singleton(
        WonState,
    )

    normal_game_mode = providers.Singleton(
        NormalGameMode
    )

    competitive_game_mode = providers.Singleton(
        CompetitiveGameMode
    )

    game_mode_processing = providers.Singleton(
        GamemodeProcessing,
        normal_game_mode = normal_game_mode,
        competitive_game_mode = competitive_game_mode
    )

    game_play = providers.Singleton(
        GamePLay,
        reader = reader,
        won_state = won_state,
        repeated_guess_state = repeated_guess_state,
        lost_state = lost_state,
        incorrect_guess_state = incorrect_guess_state,
        holding_state = holding_state,
        correct_guess_state = correct_guess_state,
        game_mode_processing = game_mode_processing
    )

    buy_merch = providers.Singleton(
        BuyMerch,
    )

    observable_high_score_concrete = providers.Singleton(
        ObservableHighScoreConcrete,
    )

    high_score_display = providers.Singleton(
        HighscoreDisplay,
    )

    hangman = providers.Singleton(
        Hangman,
        player_list = player_list,
        game_play = game_play,
        leaderboard = leaderboard,
        player = player_provider,
        message_sender = message_sender,
        username_validator = validator,
        friend_validator = friend_validator,
        buy_merch = buy_merch,
        observable_high_score_concrete = observable_high_score_concrete,
        high_score_display = high_score_display
    )

