import pytest
from unittest.mock import Mock, MagicMock
from src.Repository.db_connection import DbConnection
from src.Repository.leader_board_repository import LeaderBoardRepository


def test_that_leaders_are_gotten():
    # Arrange
    connection = Mock(DbConnection)
    repeo = LeaderBoardRepository(connection)

    connection.execute.return_value = [("steven", 10), ("john", 39)]

    #Act
    leaders = repeo.get_leaders()

    # Arrange
    assert connection.execute.called == True
    assert type(leaders) == list
    assert type(leaders[0]) == tuple
    assert type(leaders[0][0]) == str
    assert type(leaders[0][1]) == int
