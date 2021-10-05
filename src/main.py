import random

class Hangman:
    def __init__(self):
        game_mode = ""


    def welcome_screen(self):
        print('-------------------------------------------------------')
        print("|                !WELCOME TO HANGMAN!                 |")
        print('-------------------------------------------------------')
        print("**                                                   **")
        print("**                 Already a Player?                 **")
        print("**           Input your username to log in           **")
        print("**                                                   **")
        print("**                        OR                         **")
        print("**                 Input: 'new user'                 **")
        print("**                                                   **")
        print("**                                                   **")
        print('-------------------------------------------------------')
        user_input = input("Input:")
        if user_input == "new user":
            pass
        else:
            self.main_menu(user_input)
    
    def main_menu(self, username):
        print('-------------------------------------------------------')
        print("                     HI",username,"!                   ")
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
            self.game_mode_menu()
        elif menu_input == "m":
            self.game_mode_menu()
        elif menu_input == "l":
            self.game_mode_menu()
        else:
            self.main_menu(username)


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
            game_mode = "normal"
            self.category_menu()
        else:
            game_mode = "competitive"
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
            self.game_difficulty_menu()
        elif category_input == "c":
            self.game_difficulty_menu()
        elif category_input == "f":
            self.game_difficulty_menu()
        elif category_input == "r":
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
            self.play()
        elif difficulty_input == "m":
            self.play()
        elif difficulty_input == "h":
            self.play()
        else:
            self.game_difficulty_menu()

    def play():
        pass





if __name__ == '__main__':
    game = Hangman()
    game.welcome_screen()