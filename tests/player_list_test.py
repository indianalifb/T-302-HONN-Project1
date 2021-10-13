import pytest
from unittest.mock import Mock, MagicMock

from src.Repository.user_name_repository import UserNameRepository
from src.username_validator import UsernameValidator
from src.Players.players_list import PlayersList

def test_that_add_adds_user():
    # Arrange
    repo = MagicMock(UserNameRepository)
    validator = Mock(UsernameValidator)
    PList = PlayersList(repo, validator)

    validator.return_value.validate.return_value = True
    repo.return_value.get_username.return_value = True
    # Act
    boolean = PList.add("steven")
    lookup = PList.lookup("steven")
    # Assert
    assert lookup == True
    assert boolean == True

def test_that_add_does_not_work_for_bad_user_name():
    # Arrange
    repo = MagicMock(UserNameRepository)
    validator = Mock(UsernameValidator)
    PList = PlayersList(repo, validator)
    repo.get_username.return_value = None
    validator.validate.return_value = False

    # Act
    boolean = PList.add("Steven Hawking Peters")
    lookup = PList.lookup("Steven Hawking Peters")
    # Assert
    assert lookup == False
    assert boolean == False

def test_add_high_score():
    # Arrange
    repo = MagicMock(UserNameRepository)
    validator = Mock(UsernameValidator)
    PList = PlayersList(repo, validator)

    # Act
    PList.add_high_score('steven', 12)

    # Assert
    assert repo.save_high_score.called == True
