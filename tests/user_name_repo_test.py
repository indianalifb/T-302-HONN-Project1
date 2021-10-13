import pytest
from unittest.mock import Mock, MagicMock, patch, call
from src.Repository.user_name_repository import UserNameRepository
from src.Repository.db_connection import DbConnection
from src.username_validator import UsernameValidator

def test_that_save_username_saves():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock(UsernameValidator)
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = ["Steven"]
    # Act
    repo.save_username("Steven")

    # Assert
    assert connection.execute.called == True
    assert connection.commit.called == True
    assert repo.get_username("Steven") == "Steven"

def test_that_save_username_does_not_save_bad_names():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock(UsernameValidator)
    repo = UserNameRepository(connection, validator)
    validator.validate.return_value = False
    connection.execute.return_value = []
    # Act
    repo.save_username("Steven Hawking Jones Man")

    # Assert
    assert connection.execute.called == False
    assert connection.commit.called == False
    assert repo.get_username("Steven Hawking Jones Man") == None
def test_that_get_username_gets_calls_database():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = ["Steven"]
    # Act
    username = repo.get_username("Steven")
    # Assert
    assert username == "Steven"

def test_that_get_username_returns_none_if_no_user_is_found():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = []
    # Act
    username = repo.get_username("Maggi Mix")
    # Assert
    assert username == None

def test_that_are_friends_returns_true_when_users_are_friends():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = [1,2,3,4]
    # Act
    boolean = repo.are_friends("Steven", "Spielberg")
    # Assert
    assert boolean == True


def test_that_are_friends_returns_true_when_users_are_friends():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = []
    # Act
    boolean = repo.are_friends("Steven", "Spielberg")
    # Assert
    assert boolean == False

def test_that_high_score_is_saved():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    #Act
    repo.save_high_score(10, "Steven")
    # Assert
    assert connection.execute.called == True

def test_that_friends_are_added():
    # Arrange
    connection = Mock(DbConnection)
    validator = Mock()
    repo = UserNameRepository(connection, validator)
    connection.execute.return_value = [1,2]
    # Act
    repo.add_friend("steven", "peter")
    # Assert
    assert connection.execute.called == True
    assert connection.execute.called == True
    assert repo.are_friends("steven", "peter") == True
