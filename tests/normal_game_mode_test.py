import pytest
from unittest.mock import Mock, MagicMock

from src.GameMode.normal_gamemode import NormalGameMode

def test_normal_game_mode():
    normal_game = NormalGameMode
    
    normal_game.nr_of_guesses.return_value = 10
    normal_game.minus_points.return_value = 10
    normal_game.total_points.return_value = 100
    # Act
    guesses = normal_game.nr_of_guesses(normal_game)
    minus = normal_game.minus_points(normal_game)
    total = normal_game.total_points(normal_game)
    # Assert
    assert guesses == 10
    assert minus == 10
    assert total == 100


