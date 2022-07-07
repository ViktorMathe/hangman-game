import random
import sys
from os import system, name

words = open("words.txt", "r").split()

correctLetters = ''
wrongLetters = ''


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
    user = input("\nWhat is your name? : ")
    print(f"\nWelcome {user}, enjoy the game!\n")
    print(hangmans[0])




def instructions():
    """
    This will tell you how to play the game
    """
    clear()
    logo()
    print("""
    When you start the game you have to type your name in and press enter then the game starts.\n
    You will see empty dashes which is shows you how many letters are in the random word \n
    what you have to guess letter by letter or if you confident you can type the whole word. \n
    You have 6 wrong attemps before the game is finished,\n
    if you can guess it before you can see all the body parts on the gallow you WIN! /n
    """)
    while True:
        try:
            ready = input("Are you ready for the game? Y/N : ")
            if ready == 'y':
                startgame()
                break
            elif ready == 'n':
                main_menu()
                break
            else:
                print("Invalid choice please type Y for yes or N for no!")
        except ValueError:
            print("Wrong input been made")


menu = {}
menu['1'] = 'Start game'
menu['2'] = 'Instructions'
menu['3'] = 'Exit game'


def main_menu():

    """
    Menu to start a game or read the instructions to how to play!
    """
    clear()
    logo()
    choice = input("""
                    1.Start Game
                    2.Instructions
                    3.Exit game
                 """)
    if choice == '1':
        startgame()
    elif choice == '2':
        instructions()
    elif choice == '3':
        sys.exit()
    elif choice == '':
        None
    else:
        print('Invalid choice,please choose from option 1,2 or 3!')


main_menu()
