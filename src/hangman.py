import sys
from src.merch.sweater import Sweater
from src.merch.pants  import Pants
from src.merch.print_logo import PrintLogo
from src.merch.print_name import PrintName
from src.friend_validator import FriendValidator
from src.game_play import GamePLay
from src.message_sender import MessageSender
from src.player import Player
from src.username_validator import UsernameValidator
from src.Players.players_list import PlayersList
from src.leaders.leaders import LeaderBoard
from src.game_play import GamePLay
from src.buy_merch import BuyMerch
from src.Observer.observable_high_score import ObservableHighScoreConcrete
from src.Observer.HighscoreDisplay import HighscoreDisplay


class Hangman:
    def __init__(self, player_list: PlayersList, leaderboard: LeaderBoard, game_play: GamePLay, 
    player: Player, message_sender: MessageSender, username_validator: UsernameValidator, 
    friend_validator: FriendValidator, buy_merch: BuyMerch, 
    observable_high_score_concrete: ObservableHighScoreConcrete, high_score_display: HighscoreDisplay, 
    sweater: Sweater, pants: Pants):

        self.username = ""
        self.game_mode = ""
        self.game_difficulty = ""
        self.game_category = ""
        self.merch = ""
        self.score = 0
        self.player_list = player_list
        self.game_play = game_play
        self.leaderboard = leaderboard
        self.message_sender = message_sender
        self.player = player
        self.username_validator = username_validator
        self.friend_validator = friend_validator
        self.buy_merch = buy_merch
        self.observable_high_score_concrete = observable_high_score_concrete
        self.high_score_display = high_score_display
        self.sweater = sweater
        self.pants = pants
        self.observable_high_score_concrete.register_observer(self.high_score_display)


        '''Every screen takes input from user and reacts occordingly'''
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        user_input = input("Input:").lower()
        if user_input == "new":
            self.new_user_screen()
        elif user_input == 'q':
            sys.exit()
        else:
            self.username = user_input
            if self.player_list.lookup(user_input): #checking if username is in database
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        try_again_username_input = input("Input:").lower()
        if try_again_username_input == "n":
            self.new_user_screen()
        elif try_again_username_input == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        username_input = input("Input:")
        if not self.player_list.lookup(username_input): #checking if username is in database
            if not self.player_list.add(username_input): #if username is not in db, add it
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        elif username_input.lower() == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        username_input = input("Input:").lower()
        if not self.player_list.lookup(username_input):
            if not self.player_list.add(username_input):
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        elif username_input == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        username_input = input("Input:").lower()
        if not self.player_list.lookup(username_input):
            if not self.player_list.add(username_input):
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        elif username_input == 'q':
            sys.exit()
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
        print("**                   Buy merchandise: 'b'            **")
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        menu_input = input("Input:").lower()
        if menu_input == "p":
            self.game_mode_menu()
        elif menu_input == "a":
            self.add_friend_menu()
        elif menu_input == "m":
            self.send_message_menu_friend_input()
        elif menu_input == "l":
            self.leaderboards_menu()
        elif menu_input == "b":
            self.buy_merchendice()
        elif menu_input == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        friend_input = input("Input:").lower()
        if friend_input == "b":
            self.main_menu()
        if (self.username_validator.validate(friend_input) and
                self.friend_validator.validate(self.username, friend_input) or
                self.friend_validator.validate(friend_input, self.username)):
            self.send_message_menu_message_input(friend_input)
        elif friend_input == 'q':
            sys.exit()
        else:
            self.friend_not_found_menu(friend_input)

    def friend_not_found_menu(self, friend_name):
        print('-------------------------------------------------------')
        print("                    Message A Friend!                  ")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**                  Username not found               **")
        print("**                                                   **")
        print("**                     back: 'b'                     **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        user_input = input("Input:").lower()
        if user_input == 'b':
            self.send_message_menu_friend_input()
        else:
            sys.exit()


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
        print("**                  Quit: 'q'                        **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        message_input = input("Input:").lower()
        if message_input == "b":
            self.main_menu()
        elif message_input == 'q':
            sys.exit()
        else:
            self.player.send_message(friend_name, message_input)
            self.main_menu()

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
        message_input = input("Input:").lower()
        if message_input == "b":
            self.main_menu()
        elif message_input == 'q':
            sys.exit()

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
            print("**                     Quit: 'q'                     **")
            print('-------------------------------------------------------')
            message_input = input("Input:").lower()
            if message_input == 'b':
                self.main_menu()
            elif message_input == 'q':
                sys.exit()

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
        print("**                  Quit: 'q'                        **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        friend_username_input = input("Input:").lower()
        if friend_username_input == "b":
            self.main_menu()
        if self.friend_validator.validate(self.username, friend_username_input):
            self.already_friends_menu()
        if self.username_validator.validate(friend_username_input) and self.player_list.lookup(friend_username_input):
            self.player.add_friend(self.username, friend_username_input)
            self.friend_added_menu()
        elif friend_username_input == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        try_again_friend_username_input = input("Input:").lower()
        if try_again_friend_username_input == "b":
            self.main_menu()
        if self.friend_validator.validate(self.username, friend_username_input):
            self.already_friends_menu()
        if self.username_validator.validate(try_again_friend_username_input) and self.player_list.lookup(try_again_friend_username_input):
            self.friend_added_menu()
        elif try_again_friend_username_input == 'q':
            sys.exit()
        else:
            self.friend_username_wrong_menu()

    def already_friends_menu():
        print('-------------------------------------------------------')
        print("|                      Lucky You!                       |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**             You guys are already friends!         **")
        print("**                                                   **")
        print("**                                                   **")
        print("**                     back: 'b'                     **")
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        input = input("Input:").lower()
        if input.lower() == 'b':
            self.main_menu()
        if input.lower() == 'q':
            sys.exit()

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
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        the_input = input("Input:").lower()
        if the_input == "p":
            self.game_mode_menu()
        elif the_input == 'q':
            sys.exit()
        else:
            self.main_menu()


    def buy_merchendice(self):
        print('-------------------------------------------------------')
        print("|                  Choose Merchandise                 |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**                    Sweater: 's'                   **")
        print("**                    Pants: 'p'                     **")
        print("**                                                   **")
        print("**                back to main menu: 'b'             **")
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        merch_type = input("Input: ")
        if merch_type == "s":
            #self.buy_merch.purchase(Sweater(),None)
            self.buy_or_extra(self.sweater)
        elif merch_type == "p":
            #self.buy_merch.purchase(Pants(),None)
            self.buy_or_extra(self.pants)
        elif merch_type == 'q':
            sys.exit()
        else:
            self.main_menu()

    def buy_or_extra(self, clothes):
        print('-------------------------------------------------------')
        print("|         Buy ",self.merch, " or add name or logo     |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**                Buy chosen merch: 'b'              **")
        print("**                    Add extra: 'e'                 **")
        print("**                                                   **")
        print("**                back to main menu: 'b'             **")
        print("**                      Quit: 'q'                    **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        user_input = input("Input: ")
        if user_input == "b":
            self.buy_merch.purchase(clothes)
            self.main_menu()
        elif user_input == "e":
            self.buy_extra(clothes)
        elif user_input == 'q':
            sys.exit()
        else:
            self.main_menu()

    def buy_extra(self,clothes):
        print('-------------------------------------------------------')
        print("|                    Choose Extra                     |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                                                   **")
        print("**               Add name to merch: 'n'              **")
        print("**               Add logo to merch: 'l'              **")
        print("**                                                   **")
        print("**               back to main menu: 'b'              **")
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        extra = input("Input: ")
        if extra == "n":
            self.buy_merch.purchase(PrintName(clothes))
            self.main_menu()
        elif extra == "l":
            self.buy_merch.purchase(PrintLogo(clothes))
            self.main_menu()
        elif extra == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        game_input = input("Input:").lower()
        if game_input == "n":
            self.game_mode = "n"
            self.category_menu()
        elif game_input == 'q':
            sys.exit()
        else:
            self.game_mode = "c"
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
        print("**                     Quit: 'q'                     **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        category_input = input("Input:").lower()
        if category_input == "a":
            self.game_category = "a"
            self.game_difficulty_menu()
        elif category_input == "c":
            self.game_category = "c"
            self.game_difficulty_menu()
        elif category_input == "f":
            self.game_category = "f"
            self.game_difficulty_menu()
        elif category_input == 'q':
            sys.exit()
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
        print("**                     Quit: 'q'                     **")
        print('-------------------------------------------------------')
        difficulty_input = input("Input:").lower()
        if difficulty_input == "e":
            self.game_difficulty = "e"
            self.score = self.game_play.play(self.game_mode , self.game_difficulty, self.game_category)
            self.observable_high_score_concrete.set_new_high_score(self.score, self.username)
            self.main_menu()
        elif difficulty_input == "m":
            self.game_difficulty = "m"
            self.score = self.game_play.play(self.game_mode , self.game_difficulty, self.game_category)
            self.observable_high_score_concrete.set_new_high_score(self.score, self.username)
            self.main_menu()
        elif difficulty_input == "h":
            self.game_difficulty = "h"
            self.score = self.game_play.play(self.game_mode , self.game_difficulty, self.game_category)
            self.observable_high_score_concrete.set_new_high_score(self.score, self.username)
            self.main_menu()
        elif difficulty_input == 'q':
            sys.exit()
        else:
            self.game_difficulty_menu()
