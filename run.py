import random
import sys
from os import system, name


def clear():
    """
    Clear the terminal if Windows it is using
    the 'cls' statement otherwise (Linux or Mac)
    it uses the 'clear' statement
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def logo():
    """
    Hangman logo
    """
    print("""
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                   """)


hangmans = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]


def startgame():
    """
    This method will start the game from scratch
    """
    clear()
    logo()
    print(hangmans[6])


def instuctions():
    """
    This will tell you how to play the game
    """
    print("This will tell you what to do")


menu = {}
menu['1'] = 'Start game'
menu['2'] = 'Instructions'
menu['3'] = 'Exit game'


def main_menu():

    """
    Menu to start a game or read the instructions to how to play!
    """
    logo()
    choice = input("""
                    1.Start Game
                    2.Instructions
                    3.Exit game
                 """)
    if choice == '1':
        startgame()
    elif choice == '2':
        instuctions()
    elif choice == '3':
        sys.exit()
    elif choice == '':
        None
    else:
        print('Invalid choice,please choose from option 1 or 2!')
        main_menu()


main_menu()