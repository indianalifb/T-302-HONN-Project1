import pytest
from unittest.mock import Mock, MagicMock

from src.GameMode.competitive_gamemode import CompetitiveGameMode

def test_normal_game_mode():
    competitive_game = CompetitiveGameMode
    
    competitive_game.nr_of_guesses.return_value = 10
    competitive_game.minus_points.return_value = 10
    competitive_game.total_points.return_value = 100
    # Act
    guesses = competitive_game.nr_of_guesses(competitive_game)
    minus = competitive_game.minus_points(competitive_game)
    total = competitive_game.total_points(competitive_game)
    # Assert
    assert guesses == 7
    assert minus == 30
    assert total == 210


