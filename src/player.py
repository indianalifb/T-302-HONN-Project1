
from src.Players.players_list import PlayersList
from src.message_sender import MessageSender

class Player:
    def __init__(self, message_sender: MessageSender, player_list: PlayersList):
        self.__message_sender = message_sender
        self.__player_list = player_list
    def add_friend(self, username, friend_username):
        pass
    def send_message(self, friend_username, message):
        self.__message_sender.send(friend_username, message)