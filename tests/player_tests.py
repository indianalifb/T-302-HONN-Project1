from src.player import Player
from src.message_sender import MessageSender
from src.friend_adder import FriendAdder
from src.Players.players_list import PlayersList
import pytest
from unittest.mock import Mock, MagicMock, patch

def test_that_player_can_send_message():
    # Arrange
    sender = Mock(MessageSender)
    list = Mock(PlayersList)
    adder = Mock(FriendAdder)
    player = Player(sender, list, adder)
    # Act
    player.send_message("Steven", "Message")
    # Assert
    assert sender.send.called == True

def test_that_player_can_add_friend():
    # Arrange
    sender = Mock(MessageSender)
    list = Mock(PlayersList)
    adder = Mock(FriendAdder)
    player = Player(sender, list, adder)
    # Act
    player.add_friend("Steven", "John")
    # Assert
    assert adder.add_friend.called == True
