import psycopg2
from src.db_connections.db_config import DbConfig
from src.Repository.db_connection import DbConnection
from src.db_connections.postgres_db_connection import PostgresDbConnection


class LeaderBoardRepository:
    def __init__(self, connection: DbConnection):
        self.__connection = connection

    def get_leaders(self):
        leaders = self.__connection.execute(
                '''SELECT * FROM LEADERBOARD'''
                )
        return leaders
