from src.Repository.user_name_repository import UserNameRepository
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection
from src.friend_validator import FriendValidator

import pytest
from unittest.mock import Mock, MagicMock


def test_that_friend_validator_returns_true_if_users_are_friends():
    # Arrange
    repo = Mock(UserNameRepository)
    connection = Mock(DbConnection)
    validator = Mock(UsernameValidator)
    friend = FriendValidator(repo, connection, validator)
    repo.return_value.are_friends.return_value = True

    # Act
    check = friend.validate("steven", "john")

    # Assert
    assert check == True


def test_that_friend_validator_returns_false_if_users_are_not_friends():
    # Arrange
    repo = Mock(UserNameRepository)
    connection = Mock(DbConnection)
    validator = Mock(UsernameValidator)
    friend = FriendValidator(repo, connection, validator)
    repo.return_value.are_friends.return_value = False

    # Act
    check = friend.validate("steven", "john")

    # Assert
    assert check == False
