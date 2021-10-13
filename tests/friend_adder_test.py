from src.friend_adder import FriendAdder
from src.Repository.db_connection import DbConnection
from src.Repository.user_name_repository import UserNameRepository
import pytest
from unittest.mock import Mock, MagicMock

# def test_that_adder_adds_friends():
#     # Arrange
#     repo = MagicMock(UserNameRepository)
#     connection = Mock(DbConnection)
#     validator = Mock()
#     adder = FriendAdder(repo, connection, validator)
#     # Act
#     adder.add_friend("Steven", "George")
#     # Assert
#     assert repo.add_friend.called == True
