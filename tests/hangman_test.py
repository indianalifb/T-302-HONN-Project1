# from pytest import *
# from unittest.mock import Mock, MagicMock
# from src.friend_validator import FriendValidator
# from src.game_play import GamePLay
# from src.message_sender import MessageSender
# from src.player import Player
# from src.username_validator import UsernameValidator
# from src.Players.players_list import PlayersList
# from src.leaders.leaders import LeaderBoard
# from src.game_play import GamePLay
# from src.buy_merch import BuyMerch
# from src.Observer.observable_high_score import ObservableHighScoreConcrete
# from src.Observer.HighscoreDisplay import HighscoreDisplay
# from unittest.mock import patch, call
# from io import StringIO
# import mock
# import sys
# from unittest import *


# from src.hangman import Hangman

# @patch('builtins.print')
# def test_welcome_screen_print(mocked_print, monkeypatch):
#     # Arrange
#     PList = MagicMock(PlayersList)
#     leaderboard = MagicMock(LeaderBoard)
#     game_play = MagicMock(GamePLay)
#     player = MagicMock(Player)
#     message_sender = MagicMock(MessageSender)
#     username_validator = MagicMock(UsernameValidator)
#     friend_validator =MagicMock(FriendValidator)
#     buy_merch = MagicMock(BuyMerch)
#     observable_high_score_concrete = MagicMock(ObservableHighScoreConcrete)
#     high_score_display = MagicMock(HighscoreDisplay)
#     hangiman = Hangman(PList, leaderboard, game_play,player,
#     message_sender,username_validator,friend_validator,
#     buy_merch,observable_high_score_concrete,high_score_display)

#     #act
#     # mock_input = StringIO('new\n')
#     # monkeypatch.setattr('sys.stdin', mock_input)
#     # hangiman.welcome_screen()
#     # #assert mocked_print.mock_calls == [call("-------------------------------------------------------\n|                !WELCOME TO HANGMAN!                 |\n-------------------------------------------------------\n**                                                   **\n**                 Already a Player?                 **\n**           Input your username to log in           **\n**                                                   **\n**                        OR                         **\n**                   Input: 'new'                    **\n**                                                   **\n**                     Quit: 'q'                     **\n-------------------------------------------------------\n")]
#     # assert mocked_print.mock_calls == [call("|                !WELCOME TO HANGMAN!                 |\n-------------------------------------------------------\n**                                                   **\n**                 Already a Player?                 **\n**           Input your username to log in           **\n**                                                   **\n**                        OR                         **\n**                   Input: 'new'                    **\n**                                                   **\n**                     Quit: 'q'                     **\n-------------------------------------------------------\n")]
#     # doNothing().when(hangiman).handleLoginResponse(any()); 
#     with mock.patch("src.hangman.print") as print_mock:
#         # mock_input = StringIO('new\n')
#         # monkeypatch.setattr('sys.stdin', mock_input)
#         hangiman.welcome_screen()
#         print_mock.assert_called_with('-------------------------------------------------------')
#         print_mock.assert_called_with("|                !WELCOME TO HANGMAN!                 |")
#         print_mock.assert_called_with('-------------------------------------------------------')
#         print_mock.assert_called_with("**                                                   **")
