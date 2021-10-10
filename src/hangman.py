import random
import os

from src.friend_validator import FriendValidator
from src.game_play import GamePLay
from src.db_connections.postgres_db_connection import PostgresDbConnection
from src.message_sender import MessageSender
from src.player import Player
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection
from src.Players.players_list import PlayersList
from src.GameMode.normal_gamemode import NormalGameMode
from src.GameMode.competitive_gamemode import CompetitiveGameMode
from src.leaders.leaders import LeaderBoard 
from src.infrastructure.settings import Settings
from src.db_connections.db_config import DbConfig
from src.game_play import GamePLay


class Hangman:
    def __init__(self, player_list: PlayersList, leaderboard: LeaderBoard, game_play: GamePLay):
        self.username = ""
        self.game_mode = ""
        self.game_difficulty = ""
        self.game_category = ""
        self.player_list = player_list
        self.game_play = game_play
        self.leaderboard = leaderboard
        self.message_sender = MessageSender() # it doesn't need to be initialized with any values so maybe this is okay?
        self.player = Player(self.message_sender, self.player_list)


    def welcome_screen(self):
        print('-------------------------------------------------------')
        print("|                !WELCOME TO HANGMAN!                 |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                 Already a Player?                 **")
        print("**           Input your username to log in           **")
        print("**                                                   **")
        print("**                        OR                         **")
        print("**                   Input: 'new'                    **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        user_input = input("Input:")
        if user_input == "new":
            self.new_user_screen()
        else:
            self.username = user_input
            if self.player_list.lookup(user_input):
                self.main_menu()
            else:
                self.wrong_username_menu()

    def wrong_username_menu(self):
        print('-------------------------------------------------------')
        print("|                      OH NO :(                       |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**                 Username not found!               **")
        print("**                     Try again!                    **")
        print("**                 Input your username               **")
        print("**                                                   **")
        print("**                   new member?: 'n'                **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        try_again_username_input = input("Input:")
        if try_again_username_input == "n":
            self.new_user_screen()
        else:
            self.username = try_again_username_input
            if self.player_list.lookup(try_again_username_input):
                self.main_menu()
            else:
                self.wrong_username_menu()


    def new_user_screen(self):
        print('-------------------------------------------------------')
        print("|                !WELCOME TO HANGMAN!                 |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                  Become a Player!                 **")
        print("**                                                   **")
        print("**                  Input a username                 **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        username_input = input("Input:")
        if not self.player_list.lookup(username_input):
            if not self.player_list.add(username_input):
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        else:
            self.username_taken_screen()

    def username_too_long_screen(self):
        print('-------------------------------------------------------')
        print("|                      OH NO :(                       |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                 Username too long!                **")
        print("**                 Try a shorter one!                **")
        print("**                  Input a username                 **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        username_input = input("Input:")
        if not self.player_list.lookup(username_input):
            if not self.player_list.add(username_input):
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        else:
            self.username_taken_screen()


    def username_taken_screen(self):
        print('-------------------------------------------------------')
        print("|                      OH NO :(                       |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                This username is taken             **")
        print("**                                                   **")
        print("**               Input another username!             **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        username_input = input("Input:")
        if not self.player_list.lookup(username_input):
            if not self.player_list.add(username_input):
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        else:
            self.username_taken_screen()


    
    def main_menu(self):
        print('-------------------------------------------------------')
        print("                     HI",self.username,"!              ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                   PLAY! : 'p'                     **")
        print("**                                                   **")
        print("**                   Add a friend : 'a'              **")
        print("**                   Send a message : 'm'            **")
        print("**                   Leaderboards : 'l'              **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        menu_input = input("Input:")
        if menu_input == "p":
            self.game_mode_menu()
        elif menu_input == "a":
            self.add_friend_menu()
        elif menu_input == "m":
            self.send_message_menu_friend_input()
        elif menu_input == "l":
            self.leaderboards_menu()
        else:
            self.main_menu()

    def send_message_menu_friend_input(self):
        print('-------------------------------------------------------')
        print("                    Message A Friend!                  ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**               Input friend's username!            **")
        print("**                                                   **")
        print("**                  back: 'b'                        **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        friend_input = input("Input:")
        username_validator = UsernameValidator()
        friend_validator = FriendValidator()
        if friend_input == "b":
            self.main_menu()
        if username_validator.validate(friend_input) and friend_validator.validate(self.username, friend_input): #TODO: and they are friends with the person
            self.send_message_menu_message_input(friend_input)

    def send_message_menu_message_input(self, friend_name):
        print('-------------------------------------------------------')
        print("                    Message A Friend!                  ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**               Input your message!                 **")
        print("**                                                   **")
        print("**                  back: 'b'                        **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        message_input = input("Input:")
        if message_input == "b":
            self.main_menu()
        else:
            self.player.send_message(friend_name, message_input)

    def empty_leaderboards_menu(self):
        print('-------------------------------------------------------')
        print("                      LEADERBOARDS!                    ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                 No one else is here               **")
        print("**                                                   **")
        print("**                   So I guess..                    **")
        print("**                                                   **")
        print("**                  U ARE THE BEST!                  **")
        print("**                                                   **")
        print("**                    back: 'b'                      **")
        print('-------------------------------------------------------')
        message_input = input("Input:")
        if message_input == "b":
            self.main_menu()
        # TODO: klara 

    def leaderboards_menu(self):
        leaders = self.leaderboard.get_leaders()
        if leaders == None:
            self.empty_leaderboards_menu()
            return
        else:
            print('-------------------------------------------------------')
            print("                      LEADERBOARDS!                    ")
            print('-------------------------------------------------------')
            print("**   Name                            Score           **")

            for tup in leaders:
                print("** {0:30}    {1:<16}**".format(tup[0], tup[1]))
        
            print("**                    back: 'b'                      **")
            print('-------------------------------------------------------')
            message_input = input("Input:")
            if message_input == 'b':
                self.main_menu()

    def add_friend_menu(self):
        print('-------------------------------------------------------')
        print("                     Add A new Friend!                 ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**               Input friend's username!            **")
        print("**                                                   **")
        print("**                  back: 'b'                        **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        friend_username_input = input("Input:")
        validator = UsernameValidator()
        if friend_username_input == "b":
            self.main_menu()
        if validator.validate(friend_username_input):
            # TODO: actually adding a friend through Player class

            self.friend_added_menu()
        else:
            self.friend_username_wrong_menu()

    def friend_username_wrong_menu(self):
        print('-------------------------------------------------------')
        print("|                      OH NO :(                       |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**              Friend's username not found!         **")
        print("**                     Try again!                    **")
        print("**                                                   **")
        print("**                     back: 'b'                     **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        try_again_friend_username_input = input("Input:")
        if try_again_friend_username_input == "b":
            self.main_menu()
        if UsernameValidator(try_again_friend_username_input):
            self.friend_added_menu()
        else:
            self.friend_username_wrong_menu()

    def friend_added_menu(self):
        print('-------------------------------------------------------')
        print("                  A new Friend ADDED!                  ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                 Play a game: 'p'                  **")
        print("**                                                   **")
        print("**                                                   **")
        print("**               Back to main menu: 'm'              **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        the_input = input("Input:")
        if the_input == "p":
            self.game_mode_menu()
        else:
            self.main_menu()


    def game_mode_menu(self):
        print('-------------------------------------------------------')
        print("                   Choose your game!                   ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                    Normal: 'n'                    **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                   Competitive: 'c'                **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        game_input = input("Input:")
        if game_input == "n":
            self.game_mode = "normal"
            self.category_menu()
        else:
            self.game_mode = "competitive"
            self.category_menu()

    def category_menu(self):
        print('-------------------------------------------------------')
        print("                   Choose your category!               ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                    Animals: 'a'                   **")
        print("**                    Countries: 'c'                 **")
        print("**                    Food: 'f'                      **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        category_input = input("Input:")
        if category_input == "a":
            self.game_category = "a"
            self.game_difficulty_menu()
        elif category_input == "c":
            self.game_category = "c"
            self.game_difficulty_menu()
        elif category_input == "f":
            self.game_category = "f"
            self.game_difficulty_menu()
        else:
            self.category_menu()


    def game_difficulty_menu(self):
        print('-------------------------------------------------------')
        print("                 Choose your difficulty!               ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                    Easy: 'e'                      **")
        print("**                                                   **")
        print("**                    Medium: 'm'                    **")
        print("**                                                   **")
        print("**                    Hard: 'h'                      **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        difficulty_input = input("Input:")
        if difficulty_input == "e":
            self.game_difficulty = "e"
            self.play_game()
        elif difficulty_input == "m":
            self.game_difficulty = "m"
            self.play_game()
        elif difficulty_input == "h":
            self.game_difficulty = "h"
            self.play_game()
        else:
            self.game_difficulty_menu()

    def play_game(self):
        if self.game_mode == "normal":
            self.game_play.play(NormalGameMode(), self.game_difficulty, self.game_category)
        else:
            self.game_play.play(CompetitiveGameMode(), self.game_difficulty, self.game_category)