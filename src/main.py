import random
import os
from src.db_connections.postgres_db_connection import PostgresDbConnection
from src.player import Player
from src.username_validator import UsernameValidator
from src.Repository.db_connection import DbConnection
from infrastructure.container import Container
from Players.players_list import PlayersList

def run_migrations(db_connection: DbConnection):
    dir = './migrationsrcipts'
    for filename in os.listdir(dir):
        with open(f'{dir}/{filename}') as fileobj:
            db_connection.execute(fileobj.read())
        db_connection.commit()

def create_postgres_db_config(settings: Settings):

    return PostgresDbConnection(db_config=DbConfig(
        host=settings.postgres_log_host,
        user=settings.postgres_log_user,
        password=settings.postgres_log_password,
        database=settings.postgres_log_database
        ))

class Hangman:
    def __init__(self):
        container = Container()
        self.username = ""
        self.game_mode = ""
        self.game_difficulty = ""
        self.game_category = ""


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
            if PlayersList.lookup(user_input):
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
            if PlayersList.lookup(user_input):
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
        if PlayersList.lookup(username_input):
            if PlayersList.add(username_input) == None:
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
        if PlayersList.lookup(username_input):
            if PlayersList.add(username_input) == None:
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
        if PlayersList.lookup(username_input):
            if PlayersList.add(username_input) == None:
                self.username_too_long_screen()
            else:
                self.username = username_input
                self.main_menu()
        else:
            self.username_taken_screen()


    
    def main_menu(self):
        print('-------------------------------------------------------')
        print("                     HI",self.username,"!                   ")
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
            self.send_message_menu()
        elif menu_input == "l":
            self.leaderboards_menu()
        else:
            self.main_menu()

    def send_message_menu(self):
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
        message_input = input("Input:")
        if message_input == "b":
            self.main_menu()
        # TODO: klara send message
    
    def leaderboards_menu(self):
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
        if friend_username_input == "b":
            self.main_menu()
        if UsernameValidator(friend_username_input):
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
        print("**                    Random: 'r'                    **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        category_input = input("Input:")
        if category_input == "a":
            self.game_category = "animals"
            self.game_difficulty_menu()
        elif category_input == "c":
            self.game_category = "countries"
            self.game_difficulty_menu()
        elif category_input == "f":
            self.game_category = "food"
            self.game_difficulty_menu()
        elif category_input == "r":
            self.game_category = "random"
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
            self.game_difficulty = "easy"
            self.play()
        elif difficulty_input == "m":
            self.game_difficulty = "medium"
            self.play()
        elif difficulty_input == "h":
            self.game_difficulty = "hard"
            self.play()
        else:
            self.game_difficulty_menu()

    def play():
        pass





if __name__ == '__main__':
    game = Hangman()
    game.welcome_screen()
