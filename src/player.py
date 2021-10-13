
from src.Players.players_list import PlayersList
from src.message_sender import MessageSender
from src.friend_adder import FriendAdder
class Player:
    def __init__(self, message_sender: MessageSender, player_list: PlayersList, friend_adder: FriendAdder):
        self.__message_sender = message_sender
        self.__player_list = player_list
        self.__friend_adder = friend_adder

    def add_friend(self, username, friend_username):
        self.__friend_adder.add_friend(username, friend_username)

    def send_message(self, friend_username, message):
        self.__message_sender.send(friend_username, message)
